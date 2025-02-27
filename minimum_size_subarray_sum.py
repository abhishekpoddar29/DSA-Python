'''Sliding window problem '''

def min_size_subarray(arr,target):
    n=len(arr)
    start=0
    cur_sum=0
    min_len=float('inf')
    for i in range(n):
        cur_sum+=arr[i]
        while cur_sum>=target:
            min_len=min(min_len,i-start+1)
            cur_sum-=arr[start]
            start+=1
    if min_len==float('inf'):
        return 0
    else:
        return min_len
arr=[2,3,1,2,4,3]
target=7
print(min_size_subarray(arr,target))
