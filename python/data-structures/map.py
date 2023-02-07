class MyMap:
    def __init__(self):
        self.data = {}

    def add(self, key, val):
        self.data[key] = val

map = MyMap()
map.add(1, 'a')
map.add(2, 'b')
map.add(3, 'c')

print(map.data)
print(map.data[1])
print(map.data.get(1))

# Iterate data
for i in map.data:
  print(i)

# Iterate key
for i in map.data.keys():
  print(i)

# Iterate values
for i in map.data.values():
  print(i)

