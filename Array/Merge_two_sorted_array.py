def sort_merge(nums1,nums2):
    arr=nums1+nums2
    arr.sort()
    return arr

nums1_input = input("Enter numbers for nums1 separated by spaces: ")
nums1 = list(map(int, nums1_input.split()))

nums2_input = input("Enter numbers for nums2 separated by spaces: ")
nums2 = list(map(int, nums2_input.split()))
array=sort_merge(nums1,nums2)
print(array)
