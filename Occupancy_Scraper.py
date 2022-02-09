#!/usr/bin/env python3
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import threading

INTERVAL = 1 * 60 # Seconds between website checks
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0'}

Details_south = ['https://physiqfitness.com/south-salem/', './data/south_data.txt']
Details_downtown = ['https://physiqfitness.com/downtown-salem/', './data/downtown.txt']
Details_keizer = ['https://physiqfitness.com/keizer/', './data/keizer.txt']
Details_albany = ['https://physiqfitness.com/albany/', './data/albany.txt']

Details_list = list([Details_south, Details_downtown, Details_keizer, Details_albany])

# Borrowed from stackoverflow (https://stackoverflow.com/questions/2697039/python-equivalent-of-setinterval)
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

# Scrapes link for current class - should return number of occupants.
def get_occupancy(URL):
  page = requests.get(URL, headers=HEADERS)
  soup = BeautifulSoup(page.content.decode(), 'html.parser')
  number = soup.find(class_='current').string.strip()
  return number

# Formats data and logs it to file
def task():
  for e in Details_list:
    current_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    number = get_occupancy(e[0])
    data = list([current_time, number])
    with open(e[1], 'a') as ofile:
      ofile.write(str(data)+'\n')

task()
set_interval(task, INTERVAL)

