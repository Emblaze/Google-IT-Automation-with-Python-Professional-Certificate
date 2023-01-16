#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free / du.total * 100
  return free > 20

def check_cpu_usage():
  usage = psutil.cpu_percent(1)
  return  usage < 70

"""Main body of script that checks if the 2 conditions described in the 2 functions are false
"""
if not check_disk_usage("/") or not check_cpu_usage():
  print("Error!")
else:
  print("Everything is OK!")
