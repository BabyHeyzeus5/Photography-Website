import os
from PIL import Image

#----------CONFIGURATIONS-------------#

name = 'spring-break' #album/file name (SHOULD BE THE SAME)
compress = True # True if first time import, False if just updating

#-------------------------------------#
targetFolder = f".\\pages\\albums\\{name}"
targetFile = f".\\pages\\{name}.html"
albumName = name

def compressImages(folder):
    photos = os.listdir(folder)
    i = 0
    #check for boolean
    if compress:
        compressionVal = 50
    else:
        compressionVal = 95
    #loop through photos
    for photo in photos:
        filePath = os.path.join(targetFolder, photo)
        picture = Image.open(filePath)
        exif_data = picture.info.get("exif")
        #save and add to count
        picture.save(filePath, "JPEG", optimize=True, subsampling=0, quality=compressionVal, exif=exif_data if exif_data else b'')
        i += 1
        print(f"finished {i} photos")
    return

def generateHTML(folder):
    photos = os.listdir(folder)
    html_string = "\t\t\t<img src=\"./albums/{}/{}\" alt=\"Photo in Album\" class=\"preview-size\">\n"
    messageList = []
    for photo in photos:
        messageList.append(html_string.format(albumName, photo, albumName, photo))
    return messageList

def appendFile(file, htmls):
    #begin going through the target file until the START condition is found
    fileString = []
    with open(targetFile, newline='') as file:
        for line in file:
            fileString.append(line)
            if line.strip() == "<!--START-->":
                #begin adding the photos in
                for html in htmls:
                    fileString.append(html)
        file.close()
        file2 = open(targetFile, 'w', newline='')
        for line in fileString:
            file2.write(line)
        file2.close()
        print(f"Finished. Added {len(htmls)} photos.")

compressImages(targetFolder)
htmls = generateHTML(targetFolder)
appendFile(targetFile, htmls)