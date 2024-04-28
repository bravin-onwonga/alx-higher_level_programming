#!/usr/bin/python3

"""
List 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import sys
import requests

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(owner, repo))
    data = res.json()
    i = 0
    while (i < 10):
        if !(data[i]):
            break
        sha = data[i].get('sha')
        name = data[i].get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
        i += 1
