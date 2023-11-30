#!/bin/bash
# use allow with curl
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
