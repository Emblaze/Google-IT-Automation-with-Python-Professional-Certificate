#!/usr/bin/env python3

import emails
import datetime
import os
import reports

def buildDescriptionsDict(descriptions):
  descriptionsList = []
  for textfile in descriptions:
    description = {}
    with open(os.path.join(descriptionsDir, textfile)) as content:
        lines = content.readlines()
        # print(lines, len(lines))
        description["name"] = lines[0].strip('\n')
        description["weight"] = lines[1]#.strip('\n')
        descriptionsList.append(description)
  return descriptionsList

def buildParagraph(descriptionsList):
  paragraph = []
  for pair in descriptionsList:
    paragraph.append()

if __name__ == "__main__":
  user = os.getenv('USER')
  descriptionsDir = 'supplier-data/descriptions'
  descriptions = os.listdir(descriptionsDir)
  descriptionsList = buildDescriptionsDict(descriptions)
  print(descriptionsList)
  today = datetime.datetime.now()
  title = 'Processed Update on ' + today.strftime("%B %d, %Y")
  # paragraph = "<br/>".join(descriptionsList) + "<br/>"
  reports.generate_report('/tmp/processed.pdf', title, paragraph)
  email_subject = 'Upload Completed - Online Fruit Store'  # subject line give in assignment for email
  email_body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'  # body line give in assignment for email 
  msg = emails.generate_email("automation@example.com", "{}@example.com".format(user),
                         email_subject, email_body, "/tmp/processed.pdf")  # structuring email and attaching the file. Then sending the email, using the cus$
  emails.send_email(msg)