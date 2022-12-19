#!/usr/bin/python3
"""Error code #0"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as res:
            response = res.read().decode('utf-8')
            print(response)
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
