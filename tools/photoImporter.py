import os
from PIL import Image

def setPath(name):
    targetFolder = f".\\pages\\albums\\{name}"
    targetFile = f".\\pages\\{name}.html"
    return targetFile, targetFolder

def compressImages(folder, compress):
    photos = os.listdir(folder)
    i = 0
    #check for boolean
    if compress == 'True':
        compressionVal = 50
        #loop through photos
        for photo in photos:
            filePath = os.path.join(folder, photo)
            print(filePath)
            picture = Image.open(filePath)
            exif_data = picture.info.get("exif")
            picture.thumbnail([3000,2000], Image.ANTIALIAS)
            #save and add to count
            filePath = filePath.replace("JPG", "png")
            filePath = filePath.replace("jpg", "png")
            picture.save(filePath, "PNG")
            i += 1
            print(f"finished compressing {i} photos")
    return

def generateHTML(folder, name):
    photos = os.listdir(folder)
    html_string = "\t\t\t<img src=\"../albums/{}/{}\" alt=\"Photo in Album\" class=\"preview-size\">\n"
    messageList = []
    for photo in photos:
        if "JPG" in photo or "jpg" in photo:
            continue
        messageList.append(html_string.format(name, photo))
    return messageList

def appendFile(targetFile, htmls):
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

if __name__ ==  "__main__":
    name = input("album/file name:\t") #album/file name (SHOULD BE THE SAME)
    compress = input("Compress Images (FIRST TIME IMPORT ONLY):\t") # True if first time import, False if just updating

    targetFolder = f".\\pages\\albums\\{name}"
    targetFile = f".\\pages\\{name}\\{name}.html"
    albumName = name
    
    compressImages(targetFolder, compress)
    htmls = generateHTML(targetFolder, name)
    appendFile(targetFile, htmls)