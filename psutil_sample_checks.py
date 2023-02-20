#!/usr/bin/env python3
import psutil

# To check CPU usage
print("CPU usage: ", psutil.cpu_percent())
# To check disk I/O
print("Disk I/O: ", psutil.disk_io_counters())
# To check network I/O
print("Network I/O: ", psutil.net_io_counters())