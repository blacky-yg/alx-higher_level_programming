#!/usr/bin/python3
"""Response header value #0"""

import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        req_id = res.info()['X-Request-Id']
        print(req_id)
