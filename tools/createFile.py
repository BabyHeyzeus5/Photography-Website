import shutil
import photoImporter
import os

#take in the name of the new page
name = input("New File Name:\t")

#paths to proper files for copying
templatePathHTML = ".\\templates\\albumTemplate.html"
templatePathCSS = ".\\templates\\albumStyleTemp.css"
destinationPathHTML = f".\\pages\\{name}\\{name}.html"
destinationPathCSS = f".\\pages\\{name}\\{name}-style.css"
albumPath = f".\\pages\\albums\\{name}"

#create a directory for the file
os.makedirs(f".\\pages\\{name}")
#copy file over and change apropriate information
shutil.copyfile(templatePathCSS, destinationPathCSS)

#generate the html for new photos
photoImporter.compressImages(albumPath, 'True')
photoHTML = photoImporter.generateHTML(albumPath, name) 

#create a list to copy the current HTML and check for different criteria
fileList = []

#open the new files and add changes
with open(templatePathHTML, newline='') as file:
    nameDate = input("album name, location and year:\t")

    #update HTML variables
    titleHTML = f"\t<title>{name}</title>\n"
    linkCSS = f"\t<link rel=\"stylesheet\" href=\".\\{name}-style.css\">\n"
    albumTitle = f"\t\t<h1>{nameDate}</h1>\n"

    #iterate through
    for line in file:
        fileList.append(line)
        #title and link
        if line.strip() == '<!--TitleLink-->':
            fileList.append(titleHTML)
            fileList.append(linkCSS)
        #album header
        if line.strip() == '<!--NameandDate-->':
            fileList.append(albumTitle)
        #photos
        if line.strip() == '<!--START-->':
            for photo in photoHTML:
                fileList.append(photo)
    file.close()

#open the new file and start filling out the proper data
with open(destinationPathHTML, 'w', newline='') as file:
    #iterate through and write fileList
    for line in fileList:
        file.write(line)
    file.close()
    print(f"Finished. Created {destinationPathCSS} and {destinationPathHTML}. Added {len(photoHTML)} photos.")