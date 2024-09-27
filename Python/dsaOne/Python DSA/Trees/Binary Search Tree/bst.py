# creation of BST
class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNodeBST(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNodeBST(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNodeBST(rootNode.rightChild, nodeValue)

def preOrderTraversal(rootNode):  # O(n), O(n)
    if not rootNode:
        return
    
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):  # O(n), O(n)
    if not rootNode:
        return
    
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):  # O(n), O(n)
    if not rootNode:
        return
    
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

import QueueLinkedList as queue 
def levelOrderTraversal(rootNode):  # O(n), O(n)
    if not rootNode:
        return
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

def searchNodeBST(rootNode, nodeValue):     # O(logN), O(logN)
    if nodeValue == rootNode.data:
        print(nodeValue, "is FOUND!")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == None:
            print(nodeValue, "is NOT FOUND!")
        elif rootNode.leftChild.data == nodeValue:
            print(nodeValue, "is FOUND!")
            return
        else:
            searchNodeBST(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild == None:
            print(nodeValue, "is NOT FOUND!")
        elif rootNode.rightChild.data == nodeValue:
            print(nodeValue, "is FOUND!")
            return
        else:
            searchNodeBST(rootNode.rightChild, nodeValue)


# DELETION
def findMinValueNode(rootNode):      # O(logN)
    current = rootNode

    while current:
        current = current.leftChild
    
    return current

def deleteNode(rootNode, nodeValue):    # O(logN), O(logN)
    if rootNode is None:
        return rootNode
    
    # if nodeValue on LHS of BST
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
    # if nodeValue on RHS of BST
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue)
    
    else:
        # leaf node value encounter
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        # leaf node value encounter
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        # two child nodevalues encounter
        temp = findMinValueNode(rootNode)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    
    return rootNode

    
def deleteBST(rootNode):        # O(1), O(1)
    if not rootNode:
        return None

    rootNode.leftChild = None
    rootNode.rightChild = None
    rootNode.data = None

    return "BST deletion successful!"

newBST = BSTNode(None)      # O(1), O(1)
insertNodeBST(newBST, 70)
insertNodeBST(newBST, 50)
insertNodeBST(newBST, 80)
insertNodeBST(newBST, 30)
insertNodeBST(newBST, 45)
insertNodeBST(newBST, 75)
insertNodeBST(newBST, 90)

#print(newBST.data)
#print('newBST.leftChild.data', newBST.leftChild.data)
#print('newBST.rightChild.data', newBST.rightChild.data)

# DFS
#print('preOrderTraversal\n')
#preOrderTraversal( newBST)
#print('inOrderTraversal\n')
#inOrderTraversal(newBST)
#print('postOrderTraversal\n')
#postOrderTraversal(newBST)

# BFS
#levelOrderTraversal(newBST)

# SEARCH
#searchNodeBST(newBST, 30)
#searchNodeBST(newBST, 100)

#deleteNode(newBST, 45)
#deleteNode(newBST, 90)
deleteNode(newBST, 50)
levelOrderTraversal(newBST)
