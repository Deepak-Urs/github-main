class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node= node.next

    def insertSLL(self, val, location):
        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

                if tempNode == self.tail:
                    self.tail = newNode
    
    def traverseSLL(self):
        if self.head is None:
            print("SLL does not exist")
        else:
            tempNode = self.head

            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next

    def searchSLL(self, nodeValue):
        if self.head is None:
            print('SLL is empty, nodeValue not found')
        else: 
            tempNode = self.head

            while tempNode is not None:
                if tempNode.value == nodeValue:
                    return "Value found"

                tempNode = tempNode.next
            
            return "Value does not exist in the SLL"

    def deleteNode(self, location):
        if self.head is None:
            print('The SLL does not exist')
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            elif location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode is not None:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
            else:                    
                index = 0
                tempNode = self.head
                while index < location:
                    if index + 1 == location:
                        break
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    def deleteSLL(self):
        if self.head is not None:
            print('The SLL does not exist')
        else:
            self.head = None
            self.tail = None

    def reverseSLL(self, head):
        # print('in reverseSLL, head seen as')
        # print([node.value for node in sLL])
        if head is None:
            print('The SLL does not exist')
        if head == self.tail:
            return self
        else:
            # prev, curr = None, head
            
            # while curr:
            #     nextNode = curr.next
            #     curr.next = prev
            #     prev = curr
            #     curr = nextNode
            
            # return prev

            # # recursive
            newHead = head
            if head.next:
                newHead = self.reverseSLL(head.next)
                head.next.next = head
            head.next = None

            return newHead


                
    

sLL = SingleLinkedList()
# node1 = Node(1)
# node2 = Node(2)

# sLL.head = node1
# node1.next = node2
# sLL.tail = node2
sLL.insertSLL(1, 1)
sLL.insertSLL(2, 1)
sLL.insertSLL(3, 1)
sLL.insertSLL(4, 1)
sLL.insertSLL(0, 0)
sLL.insertSLL(-1, 4)


# print([node.value for node in sLL])
# sLL.traverseSLL()

# print(sLL)
# print(sLL.searchSLL(5))

# print('Delete node operation')
# print([node.value for node in sLL])
# sLL.deleteNode(0)
# sLL.deleteNode(-1)
# sLL.deleteNode(2)
# print([node.value for node in sLL])

# print('Delete SLL operation')
# print([node.value for node in sLL])
# sLL.deleteSLL()
# print([node.value for node in sLL])

print('Reverse SLL operation')
print([node.value for node in sLL])
res = sLL.reverseSLL(sLL.head)
print([node.value for node in res])
