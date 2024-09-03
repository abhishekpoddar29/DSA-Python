'''
Given an integer array arr and an integer val, remove all occurrences of val in arr in-place. The order of the elements may be changed. Then return the number of elements in arr which are not equal to val.
Consider the number of elements in arr which are not equal to val be k, to get accepted, you need to do the following things:
Change the array arr such that the first k elements of arr contain the elements which are not equal to val. The remaining elements of arr are not important as well as the size of arr.
Return k.

Example 1:
Input: arr = [3,2,2,3], val = 3
Output: arr = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of arr being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''

def remove_occ(arr,val):
    res=[]
    for i in range(len(arr)):
        if arr[i]!=val:
            res.append(arr[i])
    return res

array=[1,2,3,3,3,5]
value=3
print(remove_occ(array,value))

