class MyStack:
    def __init__(self, data):
        self.data = data

    def push(self, val):
        self.data.append(val)

    def pop(self):
        self.data.pop()

data = MyStack([])
data.push("a")
data.push("b")
data.push("c")

data.pop()

print(data.data)

# Iterate data
for i in data.data:
  print(i)
