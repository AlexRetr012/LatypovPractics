import stat
import string
import os.path
import itertools
import hashlib
import time
from threading import Thread

pass1 = "1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad"
pass2 = "3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b"
pass3 = "74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f"
count = 0
file_path = "/Users/print/Desktop/LatypovPy"

def crDictionary():
    os.chmod(file_path,stat.S_IRWXU)
    print('Saving dictionary...Please wait')
    if(os.path.exists('pass.txt')):
        print("File already exists!")
    else:
        with open ('pass.txt','w') as f:
            for i in itertools.product(string.ascii_lowercase, repeat=5):
                f.write(''.join(i) + '\n')
            print('File pass.txt' +' was created succesfully!')
        f.close()

def hashPass():
    print('Saving password hashes...Please wait')
    if(os.path.exists('hashpass.txt')):
        print("File already exists!")
    else:
        with open ('hashpass.txt','w') as f:
            f.write(pass1+'\n'+pass2 + '\n' + pass3)
        f.close()

def conToHash(text):
    encrypted = hashlib.sha256(text.encode()).hexdigest()
    return encrypted


def compare():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("Thread #1 started working ...")
    start_time = time.time()
    global count
    with open ('pass.txt','r') as f:
        answer = ''
        for i in range(26**5):
            line = f.readline()[:-1]
            convertedLine = conToHash(line)
            if(convertedLine == pass1 or convertedLine == pass2 or convertedLine == pass3):
                answer=line
                print("Found! Password = " + answer + " : Time of searching = %s seconds" % (time.time() - start_time))
                count += 1
            if count == 3:
                break
    f.close()
    pass

def compareWithThread(i,lines,n):
    os.system('clear' if os.name == 'posix' else 'cls')
    start_time = time.time()
    global count
    if(os.path.exists('pass.txt')):
        answer = ''
        print("Thread #"+str(i+1) + " started working")
        for line in range(int((len(lines)/n)*i),int((len(lines)/n)*(i+1))):
            convertedLine = conToHash(lines[line][:-1])
            if(convertedLine == pass1 or convertedLine == pass2 or convertedLine == pass3):
                answer=lines[line][:-1]
                print("Found! Password = " + answer + " Time of searching = %s seconds" % (time.time() - start_time))
                count += 1
            if count == 3:
                break
    else:
        print("Error!File doesn't exist!")
    pass

def Threads(n):
    with open('pass.txt','r') as f:
        lines = f.readlines()
        f.close
        num = (26**5)/n
        for i in range(n):
            thread = Thread(target=compareWithThread,args=(i,lines,n))
            thread.start()

def main():
    work = True
    crDictionary()
    hashPass()
    os.system('clear' if os.name == 'posix' else 'cls')
    while work:
        print("Enter the bruteforce mode")
        print("Single-thread find - 1")
        print("Multi-thread find - 2")
        check = input("Your choice >> ")
        if (check == "1"):
            compare()
            work = False
        elif (check == "2"):
            thr = input("Enter the number of threads to use >> ")
            if thr.isnumeric():
                Threads(int(thr))
                work = False
        else:
            print("Error! You have entered a wrong value! ")

if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls')
    main()