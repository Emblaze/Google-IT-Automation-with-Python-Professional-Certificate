#!/usr/bin/env python3

import csv
import datetime
from typing import KeysView
import requests

FILE_URL = "https://storage.googleapis.com/gwg-content/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()

    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    # print(lines)
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    # Let's initiliaze a per start date employee dictionnary
    employees = {}
    # Let's parse the the csv file to build the dict
    for row in reader:    
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        date = row_date.strftime('%Y-%m-%d')
        employee = row[0] + ' ' + row[1]
        # print('Date ', date, start_date)
        if row_date >= start_date:
            if date not in employees.keys():
                employees[date] = []
            employees[date].append(employee)   
    return employees

def list_newer(employees):
    for k,v in employees.items():
        print("Started on {}: {}".format(k,v))
   
def main():
    # start_date = "2020-06-01 00:00:00"
    # print("Start date:", start_date)
    get_file_lines(FILE_URL)
    start_date = get_start_date()
    get_same_or_newer(start_date)
    list_newer(get_same_or_newer(start_date))




if __name__ == "__main__":
    main()