import hashlib
import sys
import os
from datetime import datetime


def fileLister(directory):
    if not directory.endswith('/'):
        directory += '/'

    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = dirpath + os.sep + filename
            for ext in extensions:
                if filepath.endswith(ext):
                    fileMass.append(filepath)

    ''' for fileName in os.listdir(directory):
        fileAccess = directory + fileName
        if os.path.isfile(fileAccess):
            fileMass.append(fileAccess)
        else:
            continue'''

    for fileElement in fileMass:
        fileMD5 = hashlib.md5()
        with open(fileElement,'rb') as file:
            fileContent = file.read()
        fileMD5.update(fileContent)
        fileDigest = fileMD5.hexdigest()
        fileList[fileElement] = fileDigest

    for key, value in fileList.items():
        dupList.setdefault(value, set()).add(key)

    now = datetime.now()
    formattedTime = now.strftime("%d-%m-%Y-%H-%M-%S")
    outFileName = formattedTime + directory.replace('/','-') + '.txt'
    
    result = filter(lambda x: len(x)>1, dupList.values())
    with open(outFileName,'a', encoding = 'utf-8') as file:     
        for entry in result:
            print('Files: ', entry)
            fileEntry = str(entry) + '\n'
            file.write(fileEntry)
    file.close()

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
    now = datetime.now()
    formattedTime = now.strftime("%d/%m/%Y %H:%M:%S")
    if len(sys.argv) < 2:
        directory = os.getcwd()
        print('\n\t[ DUPFINDER ]: Searching for the same files in', directory,'at',formattedTime,'\n')
    elif len(sys.argv) == 2:
        directory = sys.argv[1]
        print('\n\t[ DUPFINDER ]: Searching for the same files in', directory,'at',formattedTime,'\n')
    elif len(sys.argv) > 2:
        print('\n\t[ DUPFINDER ]: Too many path given, exiting...\n')
        sys.exit(2)
    extensions = ['pdf','doc','docx','xls','xlsx','ppt','pptx','gif','jpg','jpeg','png','gif','avi','mpg','mpeg','mkv','mp3','mp4','flv']
    dupList = {}
    fileList = {}
    fileMass = []
    dirCheck(directory)
