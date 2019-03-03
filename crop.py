#!/usr/local/bin/python3

import os, requests, time

# Prepare the folders
originalFolder = 'original'
croppedFolder = 'cropped'

if not os.path.exists(croppedFolder):
    os.makedirs(croppedFolder)

# This is the URL
url = 'http://croppola.com/croppola/image.jpg?aspectRatio=1:1&maximumHeight=90%&algorithm=croppola'

# Process all pictures
for pictureFile in os.listdir(originalFolder):
    print(pictureFile)
    data = open(originalFolder + '/' + pictureFile, 'rb')
    res = requests.post(url, data=data, headers={'User-Agent' : 'py'})
    data.close()
    if res.status_code == 200:
        f = open(croppedFolder + '/' + pictureFile, 'wb')
        f.write(res.content)
        time.sleep(5)	# let other people crop
    else:
        print('Error ' + res.status_code)

