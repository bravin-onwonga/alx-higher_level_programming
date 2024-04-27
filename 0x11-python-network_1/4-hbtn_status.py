#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests package
"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    res = requests.get(url)
    body = res.text
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
