from pathlib import Path
import os
def readfileandfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1}:{items}")

def createFile():
    try:
        readfileandfolder()
        name=input("please tell your file name:-")
        p=Path(name)
        if not  p.exists():
            with open(p,"w") as fs:
                data =input("what you want to write:-")
                fs.write(data)
                
            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exist")
            
    except Exception as err:
        print(f"an error occur {err}")
        

def readfile():
    try:
        readfileandfolder()
        name=input("which file you want to read:-")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                print(data)
            print("read successfully")
        else:
            print("the file does not exist")
    except Exception as err:
        print(f"an error occur {err}")
        
def update():
    try:
        readfileandfolder()
        name=input("which file you want to update:-")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of the  file")
            print("press 2 for overwriting the data of your file")
            print("press 3 for for appending some content in your file")
            find=int(input("Please tell your response:-"))
            
            if find==1:
                name2=input("Enter yor new file name:")
                p2=Path(name2)
                p.rename(p2)
            if find==2:
                with open(p,'w') as fs:
                    data=input("tell what you want to write:")
                    fs.write(data)
            if find==3:
                with open(p,'a') as fs:
                    data=input("tell what you want to append:")
                    fs.write(data)
    except Exception as err:
        print(f"an error occur {err}")


def delete():
    try:
        readfileandfolder()
        name=input("which file you want to delete:-")
        p=Path(name)
        if(p.exists() and p.is_file()):
            os.remove(p)
            print("file is remove")
        else:
            print("file not exist")
    except Exception as err:
        print(f"an error occur {err}")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deleting a file")

check=int(input("Please tell your response:-"))
if check==1:
    createFile()
if check==2:
    readfile()
if check==3:
    update()
if check==4:
    delete()