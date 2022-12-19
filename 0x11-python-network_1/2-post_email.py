#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request and displays the body of the response."""

import sys
from urllib import request, parse

if __name__ == "__main__":
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode('utf-8')
    req = request.Request(sys.argv[1], data)
    with request.urlopen(req) as res:
        response = res.read().decode('utf-8')
        print(response)
