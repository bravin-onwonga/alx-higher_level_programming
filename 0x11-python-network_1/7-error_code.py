#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        res = requests.get(url)
        res.raise_for_status()
        print(res.text)
    except requests.exceptions.HTTPError as err:
        status = err.response.status_code
        if (status >= 400):
            print("Error code:", status)
    except Exception as e:
        pass
