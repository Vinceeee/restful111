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

md5 = streamMD5("file")
print(md5)
