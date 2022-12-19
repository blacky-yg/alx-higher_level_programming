#!/bin/bash
# Status code of a req
curl -so /dev/null -w "%{http_code}" "$1"
