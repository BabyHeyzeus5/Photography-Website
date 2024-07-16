import os
from PIL import Image

#----------EDIT THESE-----------------#
targetFolder = ".\\pages\\albums\\luke-grad"
targetFile = ".\\pages\\luke-grad.html"
albumName = targetFolder.split("\\")[-1]


def compressImages(folder):
    photos = os.listdir(folder)
    i = 0
    for photo in photos:
        filePath = os.path.join(targetFolder, photo)
        picture = Image.open(filePath)
        picture.save(filePath,"JPEG", optimize = True, subsamppling = 0, quality = 50, exif=picture.info.get("exif"))
        i += 1
        print(f"finished {i} photos")
    return

def generateHTML(folder):
    photos = os.listdir(folder)
    html_string = "\t\t\t<a target=\"_blank\" href=\".\\albums\\{}\\{}\"><img src=\".\\albums\\{}\\{}\" alt=\"Photo in Album\"></a>\n"
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