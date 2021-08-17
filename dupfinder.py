import hashlib
import sys
import os
from datetime import datetime


def fileLister(directory):
    if not directory.endswith('/'):
        directory += '/'


    for fileName in os.listdir(directory):
        fileAccess = directory + fileName
        if os.path.isfile(fileAccess):
            fileMass.append(fileAccess)
        else:
            continue

    for fileElement in fileMass:
        # print(fileElement)
        fileMD5 = hashlib.md5()
        with open(fileElement,'rb') as file:
            fileContent = file.read()
        fileMD5.update(fileContent)
        fileDigest = fileMD5.hexdigest()
        fileList[fileElement] = fileDigest

    for key, value in fileList.items():
        dupList.setdefault(value, set()).add(key)

    result = filter(lambda x: len(x)>1, dupList.values())
    for entry in result:
        print('Files: ', entry)

    now = datetime.now()
    formattedTime = now.strftime("%d/%m/%Y %H:%M:%S")
    print('\n\t[ DUPFINDER ]: Finished searching at',formattedTime,'\n')
    print()


def dirCheck(directory):
    if not os.path.isdir(directory):
        print('\n\t[ DUPFINDER ]: Wrong path, exiting...\n')
        sys.exit(3)
    else:
        fileLister(directory)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('\n\t[ DUPFINDER ]: No path given, exiting...\n')
        sys.exit(1)
    elif len(sys.argv) > 2:
        print('\n\t[ DUPFINDER ]: Too many path given, exiting...\n')
        sys.exit(2)
    directory = sys.argv[1]
    dupList = {}
    fileList = {}
    fileMass = []
    now = datetime.now()
    formattedTime = now.strftime("%d/%m/%Y %H:%M:%S")
    print('\n\t[ DUPFINDER ]: Searching for the same files in', sys.argv[1],'at',formattedTime,'\n')
    dirCheck(directory)
