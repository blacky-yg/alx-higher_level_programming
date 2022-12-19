#!/usr/bin/python3
"""Github commits"""

import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
          sys.argv[2], sys.argv[1])
    res = requests.get(url)
    response = res.json()
    try:
        for i in range(10):
            sha = response[i]['sha']
            author = response[i]['commit']['author']['name']
            print(f"{sha}: {author}")
    except IndexError:
        pass
