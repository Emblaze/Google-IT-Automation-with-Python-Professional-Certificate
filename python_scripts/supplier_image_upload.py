#!/usr/bin/env python3
from glob import glob
from pathlib import Path
import os
import requests

# This example shows how a file can be uploaded using
# The Python Requests module
# url = "http://localhost/upload/"
# with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
#     r = requests.post(url, files={'file': opened})

url = "http://localhost/upload/"
source = Path("supplier-data/images/").glob("*.jpeg")
# print(source, type(source))

for path in source:
    print(f"{path}")
    with open(path, 'rb') as opened:
        print(f"{opened}")
        r = requests.post(url, files={'file': opened})
        print("Exception:", r.raise_for_status())
