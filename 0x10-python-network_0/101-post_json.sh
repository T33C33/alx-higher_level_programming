#!/bin/bash
# Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the response body.

# Store the URL and JSON file name in variables
URL=$1
JSON_FILE=$2

# Send the POST request and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$JSON_FILE" "$URL"