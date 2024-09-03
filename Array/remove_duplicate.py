def remove_dup(arr):
    if not arr:
        return []
    unique_ele=sorted(set(arr))
    return unique_ele
arr_input = input("Enter numbers for arr separated by spaces: ")
arr = list(map(int, arr_input.split()))
print(remove_dup(arr))
