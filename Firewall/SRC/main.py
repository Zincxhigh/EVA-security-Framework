import argparse
import os 
import sys

from firewall import firewall,firewallerror

def check_root():
    if os.getuid() != 0:
        print("This script must be run as root. Exiting.")
        print("Use: sudo python main.py....")
        sys.exit(1)

if __name__ == "__main__":
    main()