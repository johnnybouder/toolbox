def in_asc_order(arr):
    return sorted(arr) == arr

arr  = [1,2,5,4]
print(in_asc_order(arr))

arr  = [1,2,4]
print(in_asc_order(arr))

arr  = [1,2,4]
print(sorted(arr, reverse=True))