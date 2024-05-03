#!/bin/bash
# Sends a request and displays only the status code of the response.
curl -s --output /dev/null --write-out "%{http_code}" "$1"
