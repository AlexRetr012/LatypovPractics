import os
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET
def createFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open (file + ".xml", "w") as f:
        rootEl = (input('Name of a root element? >> '))
        root = ET.Element(rootEl)
        loop = int((input('How much sub elements to be in root? >>')))
        i=0
        for i in range(i,loop):
            sEL = (input('Name of a sub element? >>'))
            sELval = (input('Value of a sub element? >>'))
            ET.SubElement(root,sEL).text = sELval
        ET.dump(root)
        tree = ET.ElementTree(root)
        tree.write(file + ".xml",encoding="UTF-8")
        f.close()
    if os.path.exists(file + ".xml"):
        print('File ' + file + '.xml' +' was created succesfully!')
    else:
        print('Something went wrong. File was not created or not found in a current directory')


def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a XML file >> '))
    if os.path.exists(file + ".xml"):
        with open (file + ".xml", "r") as f:
            tree=ET.parse(file + ".xml")
            root = tree.getroot()
            print('<' + root.tag + '>') 
            for child in root:
                print(' <'+child.tag + '>')
                print('  <'+child.text + '>')
            f.close()
    else:
        print('Something went wrong. File was not created or not found in a current directory')

def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    if os.path.exists(file + ".xml"):
        os.remove(file + ".xml")
    else:
        print('Something went wrong. File was not found in a current directory')

actions = {
    1: createFile,
    2: readData,
    3: deleteFile
}
def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Create a File & Write data to file')
    print('2. Read Data from File into a Console')
    print('3. Delete a file')
    print('4. Exit')

    while True:
        action = int(input('Your choice >> '))
        if action == 4:
            exit(0)
        else:
            if action in actions:
                actions[action]()

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    main()