def part(arr,low,high):
    #right most element as pivot
    pivot=arr[high]

    i=low-1
    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            #swap the element i with elememt j
            (arr[i],arr[j])=(arr[j],arr[i])
        (arr[i+1],arr[high])=(arr[high],arr[i+1])
        return i+1

def quickSort(arr,low,high):
    if low<high:
        pi=part(arr,low,high)
        #recursive call on left side
        quickSort(arr,low,pi-1)
        #rec. on right side
        quickSort(arr,pi+1,high)

arr=[9,8,6,5,4,3,2,1]
quickSort(arr,0,len(arr)-1)
print(arr) 

