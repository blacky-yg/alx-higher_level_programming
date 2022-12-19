#!/bin/bash
# Post a JSON file to a URL
curl -sL -H "content-type:application/json"  -d @"$2" -X POST "$1"
