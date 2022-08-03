def bubbleSort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


arr=[9,8,7,6,5,4,3,2,1,98,89,87,78,76,67,65,56,54,45,43,34,32,2,1]
bubbleSort(arr)

print("sorted array is :",arr)
