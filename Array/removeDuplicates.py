'''
def removeDuplicate(nums):
    mySet=set()
    for i in range(len(nums)):
        if nums[i] not in mySet:
            mySet.add(nums[i])
    return mySet

nums=[0,0,1,1,1,2,2,3,3,4]

print(removeDuplicate(nums))

'''

def removeDuplicate(nums):
    if not nums:
        return 0
    i=0
    for j in range(1,len(nums)):
        if nums[i]!=nums[j]:
            i+=1
            nums[i]=nums[j]
    return i+1

nums=[0,0,1,1,1,2,2,3,3,4]

print(removeDuplicate(nums))

