'''
Given an array of integers, find two numbers such that they add up to a specific target
number.
The function twoSum should return indices of the two numbers such that they add up to
the target, where index1 must be less than index2. Please note that your returned answers
(both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution.
'''

def twoSum(nums,target):
    dict_={}
    for i ,  j in enumerate(nums):
        compliment=target-j
        if compliment in dict_:
            return [dict_[compliment],i]
        dict_[j]=i
    

nums=[2,4,3,7,9]
target=11
res=twoSum(nums,target)
print(res)




