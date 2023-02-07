def bubbleSortArray(data):
    for i in range(0, len(data) - 2):
        for j in range(i+1, len(data) - 1):
          if(data[j] > data[j + 1]):
            temp = data[j]
            data[j] = data[j + 1]
            data[j + 1] = temp

    return data

data = [1,3,2]
print('Unsorted...')
print(data)
newData = bubbleSortArray(data)
print('Sorted...')
print(newData)
