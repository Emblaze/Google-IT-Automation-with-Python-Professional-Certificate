#!/usr/bin/env python3

import csv
import operator
import re

per_user = {}
errors = {}
# Setting regex named capture groups
regex = r"(?P<logtype>INFO|ERROR) (?P<logmessage>[\w].*) \((?P<username>[\w.].*)\)$"

with open("syslog.log") as logfile:
  # Reading logfile line by line for processing
  for line in logfile:
        # Creating a regex result match object instance 
        result = re.search(regex, line)
        # Shortnaming result named capture groups for reuse/readability
        logtype, logmessage, username = result.group('logtype'), result.group('logmessage'), result.group('username')
        # Initializing an empty dict for a yet non-present user in the per_user dict
        if result:
          if username not in per_user.keys():
            per_user[username] = {}
            per_user[username]['INFO'] = 0
            per_user[username]['ERROR'] = 0
          # Incrementing INFO value in the user dict
          if logtype == 'INFO':
            per_user[username]['INFO'] += 1
          # Incrementing ERROR value in the user dict
          if logtype == 'ERROR':
            per_user[username]['ERROR'] += 1
            # Initializing the key-value pair for a yet absent error in the errors dict
            if logmessage not in errors.keys():
              errors[logmessage] = 1
            # Incrementing error counter otherwise  
            else:
              errors[logmessage] += 1


# Sorting by VALUE (Most common to least common)
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
# errors_list = {k : v for k, v in sorted(errors.items(), key = lambda t : t[1], reverse = True)}
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

# Writing csv files

with open('user_statistics.csv', 'w', newline='') as user_statistics:
  # Inserting headers
  # per_user_list.insert(0, ('Username', 'INFO', 'ERROR'))
  rows_to_write = [['Username', 'INFO', 'ERROR']]
  writer = csv.writer(user_statistics)
  for element in per_user_list:
    username, data = element[0], element[1]
    row = []
    #print(username)
    row.append(username)
    for value in data.values():
      row.append(str(value))
    rows_to_write.append(row)
  # print(rows_to_write)
  writer.writerows(rows_to_write)

with open('error_message.csv', 'w', newline='') as error_messages:
  # Inserting headers
  errors_list.insert(0, ('Error', 'Count'))
  writer = csv.writer(error_messages)
  writer.writerows(errors_list)