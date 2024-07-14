#!/usr/bin/python3
"""
This module retrieves the value of the 'X-Request-Id' header from a given URL.
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.getheader('X-Request-Id')
        print(header)
