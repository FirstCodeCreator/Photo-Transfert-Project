# Jeffrey Gamelin
# Photo Transfer Project
import os
from pyfiglet import Figlet

info = True


def main():

    f = Figlet(font="roman")
    print(f.renderText("Welcome to the Photo Transfer Project!"))

    fileExtensions = [".jpg", ".png", ".dng", ".orf", ".arw", ".heic", ".mov", ".mp4"]

    sourceFolder = selectSourceFolder()

    allFiles = createListOfAllFiles(sourceFolder, fileExtensions)
    filesToTransfer = allFiles[0]
    filesNotToTransfer = allFiles[1]
    years, dateList = checkFilesForTheirDate(filesToTransfer)
    destinationFolders = selectDestinationFolder([2018, 2022])
    ############################################################################################################################### remove example
    #Tranfer

def selectSourceFolder():
    sourceFolder = input("Select the source folder or the letter of the drive:")

    # set the input for the bas eof a drive if just a letter was entered (ex: i -> I:\)
    if len(sourceFolder) == 1:
        sourceFolder = sourceFolder.upper() + ":\\"

    # print selected folder
    if info:
        print("You have selected the folder " + sourceFolder)

    return sourceFolder


def createListOfAllFiles(sourceDirectory, extensions):
    # https://www.kite.com/python/answers/how-to-list-all-subdirectories-and-files-in-a-given-directory-in-python
    filesToTransfer = []
    filesNotToTransfer = []

    for root, subdirectories, files in os.walk(sourceDirectory):
        for file in files:
            for extension in extensions:
                if file.lower().endswith(extension):
                    filesToTransfer.append(os.path.join(root, file))
                    break
            if os.path.join(root, file) not in filesToTransfer:
                filesNotToTransfer.append(os.path.join(root, file))

    if info:
        print("Files to transfer:")
        for i in filesToTransfer:
            print(i)
        print("Files not to transfer:")
        for i in filesNotToTransfer:
            print(i)

    return [filesToTransfer, filesNotToTransfer]


def checkFilesForTheirDate(filesToTransfer):
    years = []
    dateList = []

    #https://www.geeksforgeeks.org/python-datetime-module/
    #https://docs.python.org/3/library/datetime.html
    #https://www.w3schools.com/python/python_datetime.asp
    '''
        now = datetime.datetime.utcnow()
        print(f'{now=:%Y-%m-%d}')
    '''


    return years, dateList


def selectDestinationFolder(years):
    destinationFolders = []

    if len(years) > 1:
        divideByYear = input("Do you want to divide the years by folder? (y/n)")

        if divideByYear == "y":
            for year in years:
                destinationFolders.append(input(f"Select the destination folder for {year}:"))

        elif divideByYear == "n":
            destinationFolders.append(input("Select the destination folder:"))
    else:
        destinationFolders.append(input("Select the destination folder:"))

    # print the list of destinations
    if info:
        print("Here is the list of the destination")

        for d in destinationFolders:
            print(d)

    return destinationFolders


if __name__ == '__main__':
    main()
    input("Press enter to leave")
