def missing(nums):
    nums.sort()
    #Both are efficient solutions
    for i in range(0,len(nums)):
        if i!=nums[i]:
            return i
        if i==len(nums)-1:
            return nums[i]+1
    '''
    for i,v in enumerate(nums):
        if i!=v:
            return v-1
        if i==len(nums)-1:
            return v+1
'''
nums_input=input("Enter numbers in range[0,n] seperate with space: ")

nums=list(map(int,nums_input.split()))
print(missing(nums))