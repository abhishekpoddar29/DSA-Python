'''
given an array 'nums'  and a target , return indeces of two numbers such that they add up to the targets
example:
nums=[2,7,8,9]
target=9
o/p: [0,1] i.e. indices of [2,7]

'''
'''
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
'''
def two_sum(nums,target):
    save={}
    for i in range(len(nums)):
        comp=target-nums[i]
        if comp in save:
            return [i,save[comp]]
        else:
            save[nums[i]]=i

nums=[2,7,5,9]
target=14
print(two_sum(nums,target))