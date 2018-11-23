"""
Script to remove whiteSpaces from files inside folders

"""
#! usr/bin/python3
import os
DirsList = os.listdir()
currentDir = os.getcwd() + '/'
        
def removeWhiteSpaceFromFiles(fileName, folderName):
    newFolderName = folderName + '/'
    oldFilePath = newFolderName + fileName
    newFilePath = newFolderName + fileName.strip()
    os.rename(oldFilePath, newFilePath)

def removeWhiteSpaceFromFolder(folderName):
    oldFolderName =  currentDir + folderName
    newFolderName =  currentDir + folderName.strip()
    os.rename(oldFolderName, newFolderName)
    return newFolderName

for Dir in DirsList:
    # index.md is not a folder
    if Dir in ('index.md', 'removeWhiteSpace.py'):
        continue

    newFolderName = removeWhiteSpaceFromFolder(Dir)

    # List of files inside the folder to rename
    fileList = os.listdir(newFolderName)
    
    # removing whiteSpace from every file
    for fileName in fileList:
        removeWhiteSpaceFromFiles(fileName, newFolderName)

