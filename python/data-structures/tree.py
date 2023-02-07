class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
       newNode = Node(data)
       if(self.root == None):
          self.root = newNode
       else:
          self.insertNode(self.root, newNode)

    def insertNode(self, node, newNode):
       if(newNode.data < node.data):
          if(node.left == None):
             node.left = newNode
          else:
             self.insertNode(node.left, newNode)
       else:
          if(node.right == None):
             node.right = newNode
          else:
             self.insertNode(node.right,newNode)

    def inOrder(self, node):
        if(node != None):
            self.inOrder(node.left)
            print(node.data)
            self.inOrder(node.right)

    def preOrder(self, node):
        if(node != None):
            print(node.data)
            self.inOrder(node.left)
            self.inOrder(node.right)

    def postOrder(self, node):
        if(node != None):
            self.inOrder(node.left)
            self.inOrder(node.right)
            print(node.data)

tree = BinarySearchTree()

tree.insert(1)
tree.insert(2)
tree.insert(3)

print(tree.root.data)

print('In-order...')
tree.inOrder(tree.root)
print('Pre-order...')
tree.preOrder(tree.root)
print('Post-order...')
tree.postOrder(tree.root)
