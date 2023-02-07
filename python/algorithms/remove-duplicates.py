def removeDups(arr):
    if arr == None:
        return arr

    current = None
    prev = None
    for idx, i in enumerate(arr):
        if idx == 0:
            current = i
        else:
            prev = current
            current = i

            if current == prev:
                arr.pop(idx)

    return arr

arr = [1,2,2,3,4,5,6,6]
print(removeDups(arr))
