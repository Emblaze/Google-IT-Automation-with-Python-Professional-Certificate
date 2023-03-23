#!/usr/bin/env python3
import re
import sys

logfile = sys.argv[1]
usernames = {}

with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    if result is None: # Checks if the rexgex found a match in the current line
      continue # and continues on to the next one if not
    name = result[1]
    usernames[name] = usernames.get(name, 0) + 1
print(usernames)