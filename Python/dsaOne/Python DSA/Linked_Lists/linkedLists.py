class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        res = ''
        while temp_node is not None:
            res += str(temp_node.value)
            if temp_node.next is not None:
                res += ' -> '
            temp_node = temp_node.next
        return res

    def append(self, value):
        newNode = Node(value) #O(1)
        if self.head is None:   #O(1)
            self.head = newNode
            self.tail = newNode
        else: #O(1)
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1 #O(1)
        #space complexity(sc) is O(1)

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next




new_linked_list = LinkedList()
#print(new_linked_list.length)
new_linked_list.append(10)
new_linked_list.append(20)
print(new_linked_list.length)
print(new_linked_list)
print(new_linked_list.traverse())