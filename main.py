import threading 
import time
d={}
def create(key,value,to=0):
    if key in d:
        print("Error: KEY already EXISTS") 
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): # 1GB constraint
                if to==0:
                    li=[value,to]
                else:
                    li=[value,time.time()+to]
                if len(key)<=32: 
                    d[key]=li
                else:
                    print("Error: Key length Limit") # 32 char key length constraint
            else:
                print("Error: MEMORY LIMIT Exceeded")
        else:
            print("Error: Invalid KEY_NAME! It must not contain any special symbols or numbers")

def modify(key,value):
    tm=d[key]
    li=[]

    if key not in d:
        print("Error: KEY does not exist. Enter a Valid Key")
    elif tm[1]!=0:
        if time.time()<tm[1]:
            li.append(value)
            li.append(tm[1])
            d[key]=li
        else:
            print("Error: Time-to-Live of given ",key,"has expired")
    else:
        li.append(value)
        li.append(tm[1])
        d[key]=li

def delete(key):
    if key not in d:
        print("Error: Given Key does not exist. Enter Valid Key") 
    else:
        tm=d[key]
        if tm[1]!=0:
            if time.time()<tm[1]: 
                del d[key]
                print("Key Deleted Successfully")
            else:
                print("Error: Time-to-Live of given ",key," has expired") 
        else:
            del d[key]
            print("Key Deleted Successfully")

def read(key):
    if key not in d:
        print("Error: KEY does not exist. Enter a Valid Key") 
    else:
        tm=d[key]
        if tm[1]!=0:
            if time.time()<tm[1]: 
                s=str(key)+":"+str(tm[0]) 
                return s
            else:
                print("Error: Time-to-Live of given ",key," has expired") 
        else:
            s=str(key)+":"+str(tm[0])
            return s







