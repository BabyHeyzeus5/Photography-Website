import os
import photoImporter

if __name__ == "__main__":
    #get all albums
    directory = os.listdir("./pages./albums")
    #cycle through and compress and generate the new HTML based off of the photoImporter settings
    for album in directory:
        print(f"\n\n_______________________________________\nCompressing {album}")
        target_folder = f".\\pages\\albums\\{album}"
        target_file = f".\\pages\\{album}\\{album}.html"

        photoImporter.compressImages(target_folder, "True")
        htmls = photoImporter.generateHTML(target_folder, album)
        photoImporter.appendFile(target_file, htmls)
