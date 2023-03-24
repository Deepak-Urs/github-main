from logging import root
import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            
            print(root.value.data)
            if(root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if(root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The nodevalue doesn't exist"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.data == nodeValue:
                return 'Success'

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)

        return 'Not Found'

def insertBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return 'Insert operation success!'

            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return 'Insert operation success!'

tN = TreeNode('Beverages')
cD = TreeNode('Cold Drinks')
hD = TreeNode('Hot Drinks')
fanta = TreeNode('Fanta')
pepsi = TreeNode('Pepsi')

tN.leftChild = cD
tN.rightChild = hD

# print('Search Operation')
# print(searchBT(tN, 'Cold Dris'))

print('Before printing:')
levelOrderTraversal(tN)
print('Insert Operation fanta')
print(insertBT(tN, fanta))
levelOrderTraversal(tN)
print('Insert Operation pepsi')
print(insertBT(tN, pepsi))
levelOrderTraversal(tN)
