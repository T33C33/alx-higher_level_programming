#!/usr/bin/python3

"""Fetches https://alx-intranet.hbtn.io/status using urllib"""

if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    # Send a GET request as urllib.request to the specified URL
    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
