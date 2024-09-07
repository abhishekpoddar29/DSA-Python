def square_array(nums):
    sq_list=[i**2 for i in nums]
    sq_list.sort()
    return sq_list
nums=[-4,9,2,5]
print(square_array(nums))