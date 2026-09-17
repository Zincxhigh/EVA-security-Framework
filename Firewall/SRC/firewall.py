import ipaddress
import logging
import subprocess
from pathlib import Path


class firewallerror(Exception):
    pass


class firewall:
    def __init__(self, config):
        self.config = config
        self.table = config["firewall"]["name"]

        self.wan = config["firewall"]["interfaces"].get("wan")
        self.lan = config["firewall"]["interfaces"].get("lan")

        self.input_policy = config["firewall"]["default_policy"].get("input", "drop")
        self.forward_policy = config["firewall"]["default_policy"].get("forward", "drop")
        self.output_policy = config["firewall"]["default_policy"].get("output", "accept")

        self.nat_enabled = bool(config["firewall"]["nat"].get("enabled", False))
        self.logging_enabled = bool(config["firewall"]["logging"].get("enabled", False))

        self.whitelist = self._read_ip_file("Whitelist.txt")
        self.temper = self._read_ip_file("temper.txt")
        self.blacklist = self._read_ip_file("Blacklist.txt")

        base_dir = Path(__file__).resolve().parent
        (base_dir / "logs").mkdir(exist_ok=True)

        logging.basicConfig(
            filename=str(base_dir / "logs" / "firewall.log"),
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
        )

    def _read_ip_file(self, filename):

        result = []

        base_dir = Path(__file__).resolve().parent

        path = base_dir / filename

        if not path.exists():

            return result

        with path.open("r", encoding="utf-8") as handle:

            for raw_line in handle:

                line = raw_line.strip()

                if not line or line.startswith("#"):

                    continue

                try:
                    ipaddress.ip_address(line)

                    result.append(line)

                except ValueError:

                    logging.warning("Ignoring invalid IP in %s: %s", filename, line)


        return result

    def _run_nft(self, ruleset):

        result = subprocess.run(

            ["nft", "-f", "-"],

            input=ruleset,

            text=True,

            capture_output=True,

            check=False,
        )

        if result.returncode != 0:

            raise firewallerror(result.stderr.strip() or "nft error")

        return result.stdout

    def rule_generation(self):

        rules = []

        rules.append(f"table inet {self.table} {{")


        rules.append("  chain input {")

        rules.append(f"    type filter hook input priority 0; policy {self.input_policy};")

        rules.append('    iifname "lo" accept')

        rules.append("    ct state invalid drop")

        rules.append("    ct state { established, related } accept")

        for ip in self.whitelist:

            rules.append(f"    ip saddr {ip} accept")

        for ip in self.blacklist:

            rules.append(f"    ip saddr {ip} drop")

        if self.logging_enabled:

            rules.append('    log prefix "FIREWALL DROP: " level warning')

            rules.append("    drop")

        rules.append("  }")

        rules.append("  chain forward {")

        rules.append(f"    type filter hook forward priority 0; policy {self.forward_policy};")

        rules.append("    ct state invalid drop")

        rules.append("    ct state { established, related } accept")

        rules.append("  }")

        rules.append("  chain output {")

        rules.append(f"    type filter hook output priority 0; policy {self.output_policy};")

        rules.append("  }")

        if self.nat_enabled and self.wan:

            rules.append(
                f'  chain postrouting {{ type nat hook postrouting priority 100; policy accept; oifname "{self.wan}" masquerade; }}'
            )

        rules.append("}")

        return "\n".join(rules)

    def apply(self):

        ruleset = self.rule_generation()

        logging.info("Applying ruleset to firewall")

        try:

            self._run_nft(ruleset)

        except firewallerror:

            logging.exception("Failed to apply")

            raise

        logging.info("Applied successfully")

    def show(self):

        result = subprocess.run(

            ["nft", "list", "table", "inet", self.table],

            text=True,

            capture_output=True,

            check=False,
        )

        if result.returncode != 0:

            print(result.stderr)

            return

        print(result.stdout)

    def stop(self):

        result = subprocess.run(

            ["nft", "delete", "table", "inet", self.table],

            text=True,

            capture_output=True,

            check=False,
        )

        if result.returncode != 0:

            print(result.stderr)

            return

        logging.info("Firewall stopped.")

    def test(self):

        ruleset = self.rule_generation()

        result = subprocess.run(

            ["nft", "-c", "-f", "-"],

            input=ruleset,

            text=True,

            capture_output=True,

            check=False,
        )

        if result.returncode == 0:

            print("Ruleset is valid.")

            return True

        print("Ruleset contains errors.")

        print(result.stderr)
        
        return False