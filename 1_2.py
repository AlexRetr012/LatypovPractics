from fileinput import filename
import os
file_path = "/"

def createFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    with open (file + ".txt", "w") as f:
        f.close()
    if os.path.exists(file + ".txt"):
        print('File ' + file + '.txt' +' was created succesfully!')
    else:
        print('Something went wrong. File was not created or not found in a current directory')

def writeDataToFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')

    if os.path.exists(file + ".txt"):
        print('Do you want to clear a file? (y/n)')
        choice = (input(">> "))
        os.system('clear' if os.name == 'posix' else 'cls')
        if choice == 'y' or choice == 'Y':
            print("File was cleared! Write a string below to write into a file")
            data = (input(">> "))
            os.system('clear' if os.name == 'posix' else 'cls')
            with open (file + ".txt", "w") as f:
                f.write(data + '\n')
                f.close()
            print('String has been added to a file succesfully!')
        else:
            print("Write a string below to add into a file")
            data = (input(">> "))
            os.system('clear' if os.name == 'posix' else 'cls')
            with open (file + ".txt", "a+") as f:
                f.write(data + '\n')
                f.close()
            print('A new string has been added to a file succesfully!')
    else:
        print('Something went wrong. File was not found in a current directory')

def readData():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    os.system('clear' if os.name == 'posix' else 'cls')
    if os.path.exists(file + ".txt"):
        with open (file + ".txt", "r") as f:
                print("The content of " + file + ".txt " + " is :"  +  "\n")
                print(f.read())
                f.close()
    else:
        print('Something went wrong. File was not found in a current directory')

def deleteFile():
    os.system('clear' if os.name == 'posix' else 'cls')
    file = (input ('Enter the name of a file >> '))
    if os.path.exists(file + ".txt"):
        os.remove(file + ".txt")
    else:
        print('Something went wrong. File was not found in a current directory')
 
actions = {
    1: createFile,
    2: writeDataToFile,
    3: readData,
    4: deleteFile
}

def main():
    os.system('clear' if os.name == 'posix' else 'cls')
    print('1. Create a File')
    print('2. Write Data to File')
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