#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
"""

import sys
import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = ""
    if (sys.argv[1]):
        q = sys.argv[1]
    data = {'q': q}
    res = requests.post(url, data=data)
    if (type(res.json()) is not dict):
        print("Not a valid JSON")
    elif (len(res.json()) == 0):
        print("No result")
    else:
        res_id = res.json().get('id')
        name = res.json().get('name')
        print("[{}] {}".format(res_id, name))
