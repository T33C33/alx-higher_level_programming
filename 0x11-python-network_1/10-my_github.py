#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and
uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()
        data = response.json()
        print("Your GitHub id is:", data["id"])
    except requests.exceptions.HTTPError as e:
        print("None")
