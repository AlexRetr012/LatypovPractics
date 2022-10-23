from csv import Dialect
from fileinput import filename
import os
import json
file_path = "/"

def createObject():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open (file + '.json','w') as f:
        if os.path.exists(file + ".json"):
            Dictionary = {}
            os.system('clear' if os.name == 'posix' else 'cls')
            key = input('Enter the key >>')
            value = input('Enter the value of a previous key >>')
            Dictionary[key] = value
            key = input('Enter the key >>')
            value = input('Enter the value of a previous key >>')
            Dictionary[key] = value
            key = input('Enter the key >>')
            value = input('Enter the value of a previous key >>')
            Dictionary[key] = value
            json.dump(Dictionary,f,indent=4)
            f.close()
            print('JSON File was successfully created!')
        else:
            print('Something went wrong. File was not found in a current directory')

def writeDataToFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open (file + '.json','w') as f:
        if os.path.exists(file + ".json"):
            Dictionary = {}
            os.system('clear' if os.name == 'posix' else 'cls')
            key = input('Enter the key >>')
            value = input('Enter the value of a previous key >>')
            Dictionary[key] = value
            key = input('Enter the key >>')
            value = input('Enter the value of a previous key >>')
            Dictionary[key] = value
            key = input('Enter the key >>')
            value = input('Enter the value of a previous key >>')
            Dictionary[key] = value
            json.dump(Dictionary,f,indent=4)
            f.close()
            print('JSON File was updated!')
        else:
            print('Something went wrong. File was not found in a current directory')

def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    if os.path.exists(file + ".json"):
        with open (file + ".json", "r") as f:
                print("The content of " + file + ".json " + " is :"  +  "\n")
                data = json.load(f)
                print(data)
                f.close()
    else:
        print('Something went wrong. File was not found in a current directory')
    

def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    if os.path.exists(file + ".json"):
        os.remove(file + ".json")
    else:
        print('Something went wrong. File was not found in a current directory')
    
 
actions = {
    1: createObject,
    2: writeDataToFile,
    3: readData,
    4: deleteFile
}

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Create a json File')
    print('2. Add an object to File')
    print('3. Read Data from File into a Console')
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