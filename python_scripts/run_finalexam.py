#!/usr/bin/env python3
import os
import requests
import locale

endpoint= 'http://34.72.68.150/fruits/'
descriptionsDir = 'supplier-data/descriptions'
descriptions = os.listdir(descriptionsDir)
descriptionsList = []
imageCounter = 1

for textfile in descriptions:
  description = {}
  with open(os.path.join(descriptionsDir, textfile)) as content:
    lines = content.readlines()
    print(lines, len(lines))
    description["name"] = lines[0].strip()
    description["weight"] = locale.atoi(lines[1].strip(' lbs\n'))
    description["description"] = lines[2].strip()
    description["image_name"] = '00' + str(imageCounter) + ".jpeg"
    imageCounter += 1
    descriptionsList.append(description)

print(descriptionsList)

for description in descriptionsList:
    print(description)
    call = requests.post(endpoint, data=description)
    print(call.request.url, call.request.body)
    response = requests.get(endpoint)
    print("Exceptions:", response.raise_for_status())
