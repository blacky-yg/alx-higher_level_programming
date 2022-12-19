#!/bin/bash
# Display Body size of a response

curl -sI "$1" | grep Content-Length | cut -d " " -f2
