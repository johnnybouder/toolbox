class MyQueue:
    def __init__(self, data):
        self.data = data

    def enqueue(self, val):
        self.data.append(val)

    def dequeue(self):
        self.data.pop(0)

data = MyQueue([])
data.enqueue("a")
data.enqueue("b")
data.enqueue("c")

data.dequeue()

print(data.data)

# Iterate data
for i in data.data:
  print(i)
