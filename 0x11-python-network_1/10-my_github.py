#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    basic = requests.auth.HTTPBasicAuth(username, password)
    res = requests.get('https://api.github.com/user', auth=basic)
    print(res.json().get('id'))
