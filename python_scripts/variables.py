#!/usr/bin/env python3
# script name: variables.py 
import os

print("HOME: " + os.environ.get("HOME",""))
print("SHELL: " + os.environ.get("SHELL",""))
print("FRUIT: " + os.environ.get("FRUIT", ""))
