from tkinter import N


def prime(num):
    #for 1 and 0 return false
    if (num==0 or num==1):
        return False
    #check for 2-num
    for i in range(2,num):
        if(num%i)==0:
            return False
    return True 

if __name__=="__main__":
    num=10
    for i in range(1,num):
        if (prime(i)):
            print(i)
            