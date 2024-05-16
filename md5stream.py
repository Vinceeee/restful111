import hashlib

def streamMD5(file):
    md5 = hashlib.md5()
    with open(file,"r") as f:
	while True:
            chunk = f.read(1024*1024*3) # every 3M per time
	    if not chunk:
		break
	    md5.update(chunk)

    return md5.hexdigest()

def streamSha(f: str):
    sha = hashlib.sha256()
    with open(f,"r") as f:
        while True:
            chunk = f.read(1024*1024*3)
            if not chunk:
                break
            sha.update(chunk)

    return sha.hexdigest()
