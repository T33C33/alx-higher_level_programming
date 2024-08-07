#!/usr/bin/python3
"""
This script takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
importing only urllib and sys
"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys

    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        body = response.read()

    print(body.decode('utf-8'))
