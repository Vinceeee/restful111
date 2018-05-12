#!/usr/bin/env python
from urllib2 import urlopen

def openRes(url):
    resp = urlopen(url,timeout=100)
    CHUNK = 1024*16
    with open("file","wb") as f:
	while True:
	    chunk = resp.read(CHUNK)
	    if not chunk:
		break
	    f.write(chunk)

if __name__ == "__main__":
    openRes("http://127.0.0.1:10618")
