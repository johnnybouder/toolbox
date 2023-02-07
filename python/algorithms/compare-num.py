def compareNums(arr): 
    counter = 0
    for i_idx, i in enumerate(arr):
        for j_idx, j in enumerate(arr):
            if i == j:
                print('Match: ' + str(i))
                counter += 1

    print("Matches found: " + str(counter))

arr = [1,2,3,1,2,6,7,8,8]
compareNums(arr)