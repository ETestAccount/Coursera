#!/user/bin/env python 3
import os
import sys

def check_reboot():
    """
        Return True if the computer has a pending reboot
    """
    return os.path.exists("/run/reboot-required")
def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything Ok.")
    sys.exit(0)

main()