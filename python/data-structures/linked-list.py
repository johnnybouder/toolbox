class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

node1 = ListNode('a')
node2 = ListNode('b')
node3 = ListNode('c')

node1.next = node2
node2.next = node3

linkedList = LinkedList()
linkedList.head = node1

# Iterate data
while linkedList.head is not None:
    print(linkedList.head.data)
    linkedList.head = linkedList.head.next
