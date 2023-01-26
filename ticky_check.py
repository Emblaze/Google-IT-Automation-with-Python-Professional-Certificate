#!/usr/bin/env python3

import csv
import operator
import re

per_user = {}
errors = {}
# Setting regex named capture groups
regex = r"(?P<logtype>INFO|ERROR) (?P<logmessage>[\w].*) \((?P<username>[\w.].*)\)$"

with open("syslog.log") as logfile:

# For dev/test purposes
# logfile = ['May 27 11:45:40 ubuntu.local ticky: INFO Created ticket [#1234] (someuser)',
#  'Jun 1 11:06:48 ubuntu.local ticky: ERROR Connection to DB failed (anotheruser)',
#  'Jan 31 01:29:16 ubuntu.local ticky: INFO Commented on ticket [#6518] (rr.robinson)',
#  'Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (breee)',
#  'Jan 31 00:21:30 ubuntu.local ticky: ERROR The ticket was modified while updating (sam)',
#  'Jan 31 00:21:30 ubuntu.local ticky: INFO The ticket was successful (breee)']

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


# print(per_user) # for debugging purposes
# print(errors) # for debugging purposes

# Sorting by VALUE (Most common to least common)
errors_list = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
# errors_list = {k : v for k, v in sorted(errors.items(), key = lambda t : t[1], reverse = True)}
# Sorting by USERNAME. Deviating from suggested use of a list and using a dict,
#  as it's easier for me to process the 3x2 dict into a csv file with my current Python skills and experience
per_user_list = sorted(per_user.items(), key=operator.itemgetter(0))

# print(per_user_list) # for debugging purposes
# print(errors_list) # for debugging purposes

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