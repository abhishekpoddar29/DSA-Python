'''
Given an integer array arr sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in arr.
Consider the number of unique elements of arr to be k, to get accepted, you need to do the following things:
Change the array arr such that the first k elements of arr contain the unique elements in the order they were present in arr initially. The remaining elements of arr are not important as well as the size of arr.
Return k.

Example 1:
Input: arr = [1,1,2]
Output:arr = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of arr being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

def remove_dup(arr):
    if not arr:
        return []
    unique_ele=sorted(set(arr))
    return unique_ele
arr_input = input("Enter numbers for arr separated by spaces: ")
arr = list(map(int, arr_input.split()))
print(remove_dup(arr))
