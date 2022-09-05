class Node:   
    def __init__(self, value, next_node):
        self.value = value
        self.next_node = next_node
        
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        node = self.head      
        

node1 = Node(10, None)
node2 = Node(20, None)
node3 = Node(30, None)
linkedList = SingleLinkedList()

linkedList.head = node1
linkedList.head.next = node2
linkedList.tail = node3

