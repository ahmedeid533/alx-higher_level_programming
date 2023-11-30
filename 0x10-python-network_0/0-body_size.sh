#!/bin/bash
# use curl
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
