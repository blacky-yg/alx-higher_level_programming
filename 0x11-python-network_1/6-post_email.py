#!/usr/bin/python3
"""Post an email #1"""

import sys
import requests

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=payload)
    print(res.text)
