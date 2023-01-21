#!/usr/bin/env python3

import shutil

import sys

def check_disk_usage(disk, min_absolute, min_percent):
    "Returns True if there is enough free disk space, False otherwise"
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = du.free / du.total * 100
    # Calculate how many free gigabytes are left
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True


# Check for at least 2 GB and 10% free space
if not check_disk_usage("/", 2, 10):
    print("ERROR: Not enough disk space")
    sys.exit(1)
print("Everything ok")
sys.exit(0)
# Alternate solution: restablish returns and call the function from the main one
# if __name__ == __main__:
#  check_disk_usage()
