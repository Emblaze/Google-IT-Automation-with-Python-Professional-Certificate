#!/usr/bin/env python3
import re
def rearrange_name(name):
  result = re.search(r"^([\w .)]*), ([\w .]*)$", name) # "^(\w*), (\w*\ ?\w*.?)$" worked
  if result == None:
    return name # returning "" would not account for single name input
  return "{} {}".format(result[2], result[1])

# name=rearrange_name("Kennedy, John F.")
# print(name)
# name=rearrange_name("Hopper, Grace M.")
# print(name)