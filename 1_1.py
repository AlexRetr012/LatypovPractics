#Для правильного отображения и выплонения программы требуется скачать библиотеку pywin32

#RLavin 4/10/22

import win32com.client
from ctypes import windll

def main():
    print ("---------------------------------------")

    strComputer = "." 
    objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator") 
    objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2") 
    colItems = objSWbemServices.ExecQuery("Select * from Win32_LogicalDisk") 

    for objItem in colItems:
        print ("Name: ", objItem.Name ) 
        print ("Volume Name: ", objItem.VolumeName) 
        gigs = int(int(objItem.Size) / 1024 / 1024 /1024) #Наиболее правильное округления байт в гигабайты
        print ("Size: ", objItem.Size , "bytes = ", gigs , "gigabytes")
        print ("File System: ", objItem.FileSystem) 
        print ("---------------------------------------")

if __name__ == '__main__':
    main()