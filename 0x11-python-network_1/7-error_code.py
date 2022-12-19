#!/usr/bin/python3
"""Error code #0"""

import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    try:
        res.raise_for_status()
        print(res.text)
    except Exception as e:
        print("Error code: {}".format(res.status_code))
