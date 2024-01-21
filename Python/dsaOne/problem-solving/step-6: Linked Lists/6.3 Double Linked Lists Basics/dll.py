class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeVal):
        node = Node(nodeVal)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "This DLL is created successfully!"

    def insertNodeDLL(self, nodeVal, location):
        if self.head is None:
            return "Node cannot be inserted"
        else:
            newNode = Node(nodeVal)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                idx = 0
                while idx < location - 1:
                    tempNode = tempNode.next
                    idx += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode


    def deleteNodeDLL(self, location):
        if self.head is None:
            return "Node cannot be deleted"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                curNode = self.head
                idx = 0
                while idx < location - 1:
                    curNode = curNode.next
                    id += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been deleted successfully")

    
    def reverseDLL(self):
        if self.head is None:
            return "DLL is empty"
        elif self.head == self.tail:
            return self.head
        else:
            l = self.head
            r = self.tail

            # finding mid point
            s = self.head
            ct = 1
            while s:
                ct += 1
                s = s.next
            mid = ct//2

            i = 0
            while i < mid:
                temp = l.value
                l.value = r.value
                r.value = temp

                l = l.next
                r = r.prev
                i += 1


                


dll = DoubleLinkedList()
dll.createDLL(5)
dll.insertNodeDLL(1,0)
dll.insertNodeDLL(10,-1)
dll.insertNodeDLL(15,-1)
dll.insertNodeDLL(7,2)
print([node.value for node in dll])

dll.deleteNodeDLL(-1)
dll.deleteNodeDLL(0)
dll.deleteNodeDLL(1)
print([node.value for node in dll])


dll.reverseDLL()
print([node.value for node in dll])


    