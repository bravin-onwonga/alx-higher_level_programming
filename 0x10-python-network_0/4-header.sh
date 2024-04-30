#!/bin/bash
# Sends a GET request to the URL, with a custom header
curl -s "$1" -H 'X-School-User-Id: 98'
