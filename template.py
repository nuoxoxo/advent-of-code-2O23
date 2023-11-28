import requests
import sys
import os
 
session = os.getenv('AOC_SESSION')
day = 3

print(session)

def get_input(day):
    url = "https://adventofcode.com/2022/day/" + str(day) + "/input"
    headers = {'Cookie': 'session=' + session}
    resp = requests.get(url, headers = headers)
    if resp.status_code != 200:
        sys.exit(f'{resp.status_code} ... {resp.reason} ... {resp.content}')
    return resp.text

def main():
    infile = get_input(day).split('\n')
    infile.pop()
    print(infile, f'len: {len(infile)}')

if __name__ == "__main__":
    main()

