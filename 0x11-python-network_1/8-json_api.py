#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    res = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        res.raise_for_status()
        result = res.json()
        if len(result) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(result['id'], result['name']))
    except Exception:
        print("Not a valid JSON")
