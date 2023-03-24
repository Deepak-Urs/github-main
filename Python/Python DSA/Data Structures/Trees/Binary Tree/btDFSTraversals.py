
from logging import root
import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

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
        return "The BT doesn't exist"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value.data == nodeValue:
                return 'Success'

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            
        return 'Not Found'

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return 'Successfully inserted'

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return 'Successfully inserted'

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)
            
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value is dNode:
                root.value = None
                return
            if root.value.leftChild:
                if root.value.leftChild is not None:
                    if root.value.leftChild is dNode:
                        root.value.leftChild = None
                        return
                    else:
                        customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild:
                if root.value.rightChild is not None:
                    if root.value.rightChild is dNode:
                        root.value.rightChild = None
                        return
                    else:
                        customQueue.enqueue(root.value.rightChild)
            

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return 'Deletion of node in BT not possible'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)

        while not customQueue.isEmpty():
            root = customQueue.dequeue()

            if root.value.data == node:
                dNode = getDeepestNode(newBT)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return 'The node has been successfully deleted'
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

        return 'Failed to delete the node'

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been deleted"
            

newBT = TreeNode('Drinks')
leftChild = TreeNode('Hot')
rightChild = TreeNode('Cold')
cola = TreeNode('Cola')
tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
fanta = TreeNode('Fanta')

newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild.leftChild = cola
rightChild.rightChild = fanta

# print('preOrderTraversal result: ')
# preOrderTraversal(newBT)

# print('inOrder result: ')
# inOrderTraversal(newBT)

# print('postOrder result: ')
# postOrderTraversal(newBT)

# print('levelOrder result: ')
# levelOrderTraversal(newBT)

# print('SEARCH result: ')
# print(searchBT(newBT, 'Teacup'))



# print('INSERT result :')
# print(insertNodeBT(newBT, fanta))
# levelOrderTraversal(newBT)

print('DeepestNode result: ')
deepestNode = getDeepestNode(newBT)
print(deepestNode.data)


# print('deleteDeepestNode result:')
# newNode = getDeepestNode(newBT)
# deleteDeepestNode(newBT, newNode)
# levelOrderTraversal(newBT)

# print('deleteNodeBT result:')
# deleteNodeBT(newBT, 'Coffee')
# levelOrderTraversal(newBT)

print('deleteBT result:')
deleteBT(newBT)
levelOrderTraversal(newBT)









