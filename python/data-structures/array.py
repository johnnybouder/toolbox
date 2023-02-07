class MyArray:
    def __init__(self, data):
        self.data = data

    def addToEnd(self, val):
        self.data.append(val)

    def addAtIndex(self, index, val):
        self.data.insert(index, val)
    
    def removeAtIndex(self, index):
        self.data.pop(index)

    def removeValue(self, value):
        self.data.remove(value)

    def sortArray(self):
        self.data.sort()

data = MyArray([])
data.addToEnd("c")
data.addToEnd("b")
data.addToEnd("a")

data.sortArray()

data.removeAtIndex(1)
data.removeValue('c')

data.addAtIndex(1, 'b')

print(data.data)

# Iterate data
for i in data.data:
  print(i)
