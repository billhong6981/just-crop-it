#!/usr/local/bin/python3

import os, requests, time

# Prepare the folders
originalFolder = "original"
croppedFolder = "cropped"

# Request user input
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

if not os.path.exists(croppedFolder):
    os.makedirs(croppedFolder)

# This is the URL
url = "http://croppola.com/croppola/image.jpg?aspectRatio=1:1&maximumHeight=90%&algorithm=croppola"

# Process all pictures
i = 0
for pictureFile in os.listdir(originalFolder):
    if pictureFile.endswith((".jpg", ".png", ".JPG", ".PNG")):
        print(pictureFile)
        data = open(originalFolder + "/" + pictureFile, "rb")
        res = requests.post(url, data=data, headers={"User-Agent": "py"})
        data.close()
        if res.status_code == 200:
            pictureFileName, pictureFileExt = os.path.splitext(pictureFile)
            pictureFileNameNew = '{}{}{}{}'.format(firstName, lastName, i, pictureFileExt)
            f = open(croppedFolder + "/" + pictureFileNameNew, "wb")
            f.write(res.content)
            time.sleep(5)  # let other people crop
            i += 1
        else:
            print("Error " + res.status_code)
