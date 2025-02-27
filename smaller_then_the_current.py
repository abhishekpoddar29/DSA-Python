'''
given an array of " nums" . find out how many numbers are smmaller then it. 
example:
nums=[8,1,2,2,3]
o/p: [4,0,1,1,3]
'''
def cur_small(nums):
    '''
    res=[]
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if i!=j and nums[i]>nums[j]:
                count+=1
        res.append(count)
    return res
    '''
    temp=sorted(nums)
    d={}
    for i,j in enumerate(temp):
        if j not in d:
            d[j]=i
    res=[]
    for i in nums:
        res.append(d[i])
    return res


nums=[8,1,2,2,3]
print(cur_small(nums))