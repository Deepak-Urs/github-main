class Node:
    def __init__(self, value):
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
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def traverse(self):
        curr = self.head
        while curr:
            print(curr.val)
            curr = curr.next

    def insert(self, index, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            curr = self.head
            i = 0
            while i < index-1:
                curr = curr.next
                i += 1

            newNode.next = curr.next
            curr.next = newNode
        self.length += 1

    def delete(self, index):
        if self.head is None:
            return "LL empty"
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            i = 0
            while i < index-1:
                curr = curr.next
                i += 1
            curr.next = curr.next.next
        self.length -= 1
    
    def traversalLength(self):
        curr = self.head
        if self.head == None:
            return 0
        
        count = 1
        while curr:
            curr = curr.next
            count += 1
        
        print('LL length:', count)

    def search(self, target):
        if self.head == None:
            return "LL empty!"
        
        curr = self.head
        while curr:
            if curr.value == target:
                return "Value Found in LL"
            curr = curr.next
        
        return "Value Not Found in LL"

    
        
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
print(linked_list)
linked_list.traversalLength()
print(linked_list.insert(2, 25))
print(linked_list)
linked_list.traversalLength()
linked_list.delete(3)
print(linked_list)
linked_list.traversalLength()
print(linked_list.search(200))