def loopNestedArr(arr): 
    for i_idx, i in enumerate(arr):
        for j_idx, j in enumerate(arr):
            print(arr[i_idx][j_idx])

arr = [[1,2,3],[4,5,6],[7,8,9]]
loopNestedArr(arr)