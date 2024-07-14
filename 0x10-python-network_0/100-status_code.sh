#!/bin/bash
# Send request and store the response in a temporary file
curl -s -o response.txt -w "%{http_code}" "$1"
