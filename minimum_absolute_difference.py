def minimum_dif(nums):
    nums.sort()
    min_dif=float('inf')
    for i in range(1,len(nums)):
        min_dif=min(min_dif,nums[i]-nums[i-1])
    res=[]
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==min_dif:
            res.append([nums[i-1],nums[i]])
    return res

nums=[4,2,1,3]
print(minimum_dif(nums))