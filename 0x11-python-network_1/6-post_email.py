#!/usr/bin/python3
"""
Sends a POST request to the passed URL with the email as a parameter
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, data={'email': email})
    with request.urlopen(req) as response:
        body = response.read().decode('utf-8')

    print(body)
