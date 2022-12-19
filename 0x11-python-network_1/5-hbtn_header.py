#!/usr/bin/python3
"""Response header value #1"""

import sys
import requests

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    print(res.headers.get('x-request-id'))
