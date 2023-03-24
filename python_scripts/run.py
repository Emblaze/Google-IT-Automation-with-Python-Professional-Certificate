#!/usr/bin/env python3
import os
import requests

corpweb_ip = 'https://34.29.101.67/feedback'
feedbacks_dir = '/data/feedback/'
feedbacks = os.listdir(feedbacks_dir)
feedbacks_dict = []

for textfile in feedbacks:
  feedback = {}
  with open(os.path.join(feedbacks_dir, textfile)) as content:
    lines = content.readlines()
    #print(lines, len(lines))
    feedback["title"] = lines[0].strip()
    feedback["name"] = lines[1].strip()
    feedback["date"] = lines[2].strip()
    feedback["feedback"] = lines[3].strip()
    feedbacks_dict.append(feedback)

# print(feedbacks_dict)

for feedback in feedbacks_dict:
    print(feedback)
    call = requests.post(corpweb_ip, data=feedback)
    print(call.request.url, call.request.body)
    response = requests.get(corpweb_ip)
    print(response.raise_for_status())
