import argparse
import os 
import sys

from config import load_yaml
from firewall import firewall,firewallerror

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root. Exiting.")
        print("Use: sudo python main.py....")
        sys.exit(1)

def main():

    parser = argparse.ArgumentParser(
        description="python nftables Fiewall."
    )

    parser.add_argument(
        "command",
        choices = ["start", "show", "stop", "test", "generate"],

        help="Fiewall Functions"
    )

    args = parser.parse_args()

    check_root()

    try:
        config = load_yaml()
        Firewall = firewall(config)

        if args.command == "start":

            Firewall.apply()

            print("Firewall Started.")

        if args.command == "stop":

            Firewall.stop()

            print("Firewall Stopped.")

        if args.command == "show":

            Firewall.show()

        if args.command == "test":

            Firewall.test()

        if args.command == "generate":

            Firewall.rule_generation()

    except Exception as error:
        print(f"ERROR: {error}")
        sys.exit(1)

if __name__ == "__main__":
    main()