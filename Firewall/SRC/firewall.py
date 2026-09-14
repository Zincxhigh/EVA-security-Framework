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
        self.logging_enabled = config['firewall']['logging']['enabled']

        self.whitelist = self._read_ip_file("Whitelist.txt")
        self.temper = self._read_ip_file("temper.txt")
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

def IP_DISCOVERY(self):
     
     for ip in self.whitelist:
        rules.append(f"ip saddr {ip} accept;")

     for ip in self.blocklist:
        rules.append(f"ip saddr {ip} drop;")

     if self.logging_enabled:
         rules.append(" limit rate 10/second log prefix FIREWALL DROP:")

def rule_generation(self):

     global rules
     rules = []

     rules.append(f"table inet {self.table}")

     rules.append(f""" 
     table inet {self.table}
     
     chain input {{type filter hook input priority 0; policy {self.input_policy};

       iifname "lo" accept;

       ct state invalid Drop;

       ct state established accept;

       ct state related accept; }}
""")

     print(IP_DISCOVERY)

     rules.append(""" 

      chain forward {

      type filter hook forward priority 0;

      policy %s

      ct state invalid Drop;

      ct state established

      ct state related accept;
      }
     """ % self.forward_policy)

     rules.append("""
      chain output {

      type filter hook output priority 0;

      policy %s

    }
     """ % self.output_policy)

     if self.nat_enabled and self.wan:
         rules.append("""

       chain postrouting {{

        type nat hook postrouting priority 100;

        oifname "{self.wan}" masquerade;

    }}
         """)

     rules.append("{")

     return"\n".join(rules)

# --------------------------------------------------------------------------------
#                      firewall functions
#---------------------------------------------------------------------------------

def apply(self):

    ruleset = self.rule_generation

    logging.info("Applying Ruleset to firewall")

    try:

        self._run_nft(ruleset)

    except firewallerror:

        logging.exception("Falied to apply")

        raise

    logging.info("Applied succesfully")

def show(self):

    result = subprocess.run(["nft","set","tabel", "inet", self.table],text=True,capture_output=True)

    if result.returncode != 0:

        print(result.stderr)

        return

     
       
     




