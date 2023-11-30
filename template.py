import requests
import sys
import os
 
day = 1
session = os.getenv('AOC_SESSION')
url = "https://adventofcode.com/2022/day/" + str(day) + "/input"
headers = {'Cookie': 'session=' + session}
resp = requests.get(url, headers = headers)
if resp.status_code != 200:
    sys.exit(f'{resp.status_code}\n{resp.reason}\n{resp.content}')
infile = resp.text
lines = infile.split('\n')
lines.pop()
print(lines, 'len:', len(lines))

