def search(list,key):
    for i in range(len(list)):
        if key==list[i]:
            print("found")
            print("found on index",i)
            break
    else:
        print("Not found")

list=[9,4,2,7,1,8]
key=int(input("enter the key element:"))
search(list,key)
