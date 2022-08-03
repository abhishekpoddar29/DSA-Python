from turtle import right


def mergeSort(myList):
    if len(myList)>1:
        mid=len(myList)//2
        left=myList[:mid]
        right=myList[mid+1:]
        #calling function to divide further
        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0
        while i<len(left) and  j<len(right):
            if left[i]<=right[j]:
                myList[k]=left[i]
                i+=1
            else:
                myList[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            myList[k]=left[i]
            i+=1
            k+=1

        while j<len(right):
            myList[k]=right[j]
            j+=1
            k+=1

myList=[9,8,7,6,5,4]
mergeSort(myList)
print(myList)
