'''
Given integer array nums , return True if there appears a value at least twice and return False if the numbers are distinct
example 1:
nums=[1,2,3,4]
o/p: False

example 2 :
nums=[1,2,3,1]
o/p: True
'''
#This can also be a solution taking time O(n^2)
'''
def conatinDup(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    return False 
'''
#This is more efficient solution as it takes O(1)
def containDup(nums):
    set1=set(nums)
    if len(set1)==len(nums):
        return False
    else:
        return True
nums=[1,2,3,1]
print(containDup(nums))
