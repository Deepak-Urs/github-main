import QueueLinkedList as queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return 'Insert NodeValue Operation Success!'


def preOrderTraversal(rootNode):
    if not rootNode:
        return "null"
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return "null"
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return "null"
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return "null"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()
            print(root.value.data)

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)

# does not handle non-found values
def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('Value found', rootNode.data)
        return
    elif nodeValue < rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            print('Value found', rootNode.leftChild.data)
            return
        else:
            searchNode(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if nodeValue == rootNode.rightChild.data:
            print('Value found', rootNode.rightChild.data)
            return
        else:
            searchNode(rootNode.rightChild, nodeValue)
    else:
        return 'Value not found'

def minValueNode(bstNode):
    current = bstNode
    while (current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
        print('rootNode.leftChild seen', rootNode.leftChild)
    if nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
        print('rootNode.rightChild seen', rootNode.rightChild)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode

newBST = BSTNode(None)

def deleteBST(rootNode):
    if rootNode is None:
        return 'null'
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.leftChild = None
    return 'BST delete success!'

# print(newBST.data)
# print(newBST.leftChild.data)

insertNode(newBST, 70)
insertNode(newBST, 50)
insertNode(newBST, 90)
insertNode(newBST, 30)
insertNode(newBST, 60)
insertNode(newBST, 80)
insertNode(newBST, 100)
insertNode(newBST, 20)
insertNode(newBST, 40)

# preOrderTraversal(newBST)
# inOrderTraversal(newBST)
# postOrderTraversal(newBST)
# levelOrderTraversal(newBST)

# searchNode(newBST, 79)

# print('delete', 20)
# deleteNode(newBST, 20)
# levelOrderTraversal(newBST)

deleteBST(newBST)
levelOrderTraversal(newBST)