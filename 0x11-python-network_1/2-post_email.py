#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
"""

import sys
from urllib import request, parse

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email})
    req = request.Request(url, data)
    with request.urlopen(url) as response:
        body = response.read()

    print(body)
