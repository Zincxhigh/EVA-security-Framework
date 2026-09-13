import ipaddress
import logging
import subprocess
from pathlib import Path

class firewallerror(Exception):
    pass

class firewall:
    def __init__(self, config):
        self.config = config
        self.table = config['firewall','name']

        self.wan = config['firewall']['interfaces'].get('wan')
        self.lan = config['firewall']['interfaces'].get('lan')

        self.input_policy = config['firewall']['default_policy']['input']
        self.forward_policy = config['firewall']['default_policy']['forward']
        self.output_policy = config['firewall']['default_policy']['output']


        self.nat_enabled = config['firewall']['nat']['enabled']
        self.loging_enabled = config['firewall']['logging']['enabled']

        self.whitelist = self._read_ip_file("Whitelist.txt")
        self.blacklist = self._read_ip_file("Blacklist.txt")

        Path('logs').mkdir(exist_ok=True)

        logging.basicConfig(
            filename = 'logs/firewall.log',
            level = logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
        )


# --------------------------------------------------------------------------------
#                      Utility Functions
#---------------------------------------------------------------------------------

def _read_ip_file(self, filename):
    result = []

    path = Path(filename)

    if not path.exists():
        return result

    with path.open("r") as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            try:
                ip = ipaddress.ip_address(line)
                result.append(line)
            except ValueError:
                        logging.warning(
                        "Ignoring invalid IP in %s: %s",
                        filename,
                        line
                    )

    return result

def _run_nft(self, ruleset):

     result = subprocess.run(["nft", "-f", "-"],input=ruleset, text=True,capture_output=True)

     if result.returncode != 0:
        raise firewallerror(result.stderr.strip())

     return result.stdout