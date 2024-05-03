#!/bin/bash
# Sends a request and displays only the status code of the response.
curl -s -H "$1" | grep -i "HTTP" | cut -d ' ' -f 2-
