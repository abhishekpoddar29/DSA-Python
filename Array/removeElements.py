def removeEle(nums,val):
    arr=[]
    for i in range(len(nums)):
        if nums[i]!=val:
            arr.append(nums[i])
    return len(arr)

nums=[2,3,3,2]
val=3
print(removeEle(nums,val))