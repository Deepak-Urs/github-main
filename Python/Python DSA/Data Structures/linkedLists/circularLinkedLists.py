class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def createCLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    def insertCSLL(self, val, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(val)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                idx = 0
                temp = self.head
                while idx < location-1:
                    temp = temp.next
                    idx += 1
                nextNode = temp.next
                newNode.next = nextNode
                temp.next = newNode
            return 'The node has been successfully inserted'

    def traverseCSLL(self):
        if self.head is None:
            return 'The CSLL is empty'
        else:
            temp = self.head
            while temp:
                print(temp.value)
                if temp.next == self.head:
                    break
                temp = temp.next
    
    def searchCSLL(self, value):
        if self.head is None:
            return 'The CSLL is empty'
        else:
            temp = self.head
            while temp:
                if temp.value == value:
                    return 'The value is found!'
                    # break
                else:
                    temp = temp.next
                if temp == self.head:
                    return 'The value is not found!'

    def deleteCSLLNode(self, location):
        if self.head is None:
            return 'The CSLL is empty'
        
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode
            else:
                tempNode = self.head
                count = 0
                while count < location - 1:
                    tempNode = tempNode.next
                    count += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None


            
            



cLL = CircularLinkedList()
print(cLL.createCLL(1))

print(cLL.insertCSLL(2, -1))
cLL.insertCSLL(3, -1)
cLL.insertCSLL(4, 0)
cLL.insertCSLL(5, 2)


print([node.value for node in cLL])

print('Traversal CSLL')
cLL.traverseCSLL()


print('Search CSLL---')
print(cLL.searchCSLL(9))

print('Delete CSLL Node---')
cLL.deleteCSLLNode(0)
cLL.deleteCSLLNode(-1)
cLL.deleteCSLLNode(1)

print([node.value for node in cLL])

print('Delete CSLL---')
cLL.deleteCSLL()
print([node.value for node in cLL])
