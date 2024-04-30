#!/bin/bash
# Display only body of a 200 status code response
status_code=$(curl -s -o /dev/null -w "%{http_code}" -X GET "$1")
if ["status_code" -eq 200]; then
  curl -s -X GET "$1"
fi
