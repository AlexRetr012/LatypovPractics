import zipfile
import os

def createFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a ZIP >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    zip_archive = zipfile.ZipFile(file + '.zip', mode='w')
    zip_archive.close()

def infoZIP():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a ZIP >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    zip_archive = zipfile.ZipFile(file + '.zip', "w")
    filen = (input ('Enter the name of a file to add (with extension) >> '))
    if os.path.exists(filen):
        zip_archive.write(filen)
        zip_archive.close
    else:
        print('Something went wrong. File was not found in a current directory')
        zip_archive.close()

def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a ZIP >> '))
    zip_archive = zipfile.ZipFile(file + '.zip', 'r')
    zip_archive.extractall('.')
    print('ZIP Extracted.')
    for file_info in zip_archive.infolist(): 
        print(file_info.filename, file_info.date_time, file_info.file_size)
    zip_archive.close()

def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    zip = (input ('Enter the name of a ZIP >> '))
    filen = (input ('Enter the name of a file to add (with extension) >> '))
    if os.path.exists(zip + ".zip"):
        os.remove(zip + ".zip")
    else:
        print('Something went wrong. File was not found in a current directory')
    if os.path.exists(filen):
        os.remove(filen)
    else:
        print('Something went wrong. File was not found in a current directory')

actions = {
    1: createFile,
    2: infoZIP,
    3: readData,
    4: deleteFile
}
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Create a ZIP')
    print('2. Add file to a ZIP')
    print('3. Extract all files from ZIP and show information')
    print('4. Delete a file')
    print('5. Exit')

    while True:
        action = int(input('Your choice >> '))
        if action == 5:
            exit(0)
        else:
            if action in actions:
                actions[action]()

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    main()