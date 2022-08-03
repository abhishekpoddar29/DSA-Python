def selectionSort(arr,size):
    for step in range(size):
        minIndex=step
        for i in range(step+1,size):
            if arr[i]<arr[minIndex]:
                minIndex=i
        
        (arr[step],arr[minIndex])=(arr[minIndex],arr[step])
        
arr=[9,8,7,6,5,4,3,2,1]
size=len(arr)
selectionSort(arr,size)
print(arr)