import QueueLinkedList as queue

class BinarySearchTree: # O(1)
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(rootNode, nodeValue): # O(logN)
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild == None:
            rootNode.leftChild = BinarySearchTree(nodeValue)
        else:
            insert( rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if rootNode.rightChild == None:
            rootNode.rightChild = BinarySearchTree(nodeValue)
        else:
            insert( rootNode.rightChild, nodeValue)
    
    return "Node inserted successfully!"

def preOrderTraversal(rootNode): # O(n)
    if not rootNode:
        return "Tree is empty!"
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
# pre-order: 70,50,30,20,40,60,90,80,100

def inOrderTraversal(rootNode): # O(n)
    if not rootNode:
        return "Tree is empty!"
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
# in-order: 20, 30, 40, 50, 60, 70, 80, 90, 100

def postOrderTraversal(rootNode): # O(n)
    if not rootNode:
        return "Tree is empty!"
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
# post-order: 20, 40,30, 60, 50, 80, 100, 90, 70

def levelOrderTraversal(rootNode): # O(n)
    if not rootNode:
        return "Tree is empty!"
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

# level-order: 70, 50, 90, 30, 60, 80, 100, 20, 40

def searchBST(rootNode, nodeVal):
    if nodeVal == rootNode.data:
        print("Target value found!")
    elif nodeVal < rootNode.data:
        if nodeVal == rootNode.leftChild.data:
           print("Target value found!")
        else:
            searchBST(rootNode.leftChild, nodeVal)
    elif nodeVal > rootNode.data:
        if nodeVal == rootNode.rightChild.data:
           print("Target value found!")
        else:
            searchBST(rootNode.rightChild, nodeVal)


def minValueNode(bstNode): # O(log N)
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current


def deleteNodeBST(rootNode, nodeVal): # O(log N)
    if not rootNode:
        return "BST is empty!"
    elif nodeVal < rootNode.data:
        rootNode.leftChild = deleteNodeBST(rootNode.leftChild, nodeVal)
    elif nodeVal > rootNode.data:
        rootNode.rightChild = deleteNodeBST(rootNode.rightChild, nodeVal)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp

        if rootNode.rightChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNodeBST(rootNode.rightChild, nodeVal)

    return rootNode

def deleteBST(rootNode): # O(1)
    if not rootNode:
        return "BST is empty!"
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "BST is deleted successfully!"




newBST = BinarySearchTree(None)
print(insert(newBST, 70))
print(insert(newBST, 50))
#print(newBST.data)
#print(newBST.leftChild.data)

print(insert(newBST, 90))
print(insert(newBST, 30))
print(insert(newBST, 60))
print(insert(newBST, 80))
print(insert(newBST, 100))
print(insert(newBST, 20))
print(insert(newBST, 40))

# DFS
#preOrderTraversal(newBST)
#inOrderTraversal(newBST)
#postOrderTraversal(newBST)

#BFS
#levelOrderTraversal(newBST)

# Search
#searchBST(newBST, 60)

# Delete Node
#deleteNodeBST(newBST, 60)
#levelOrderTraversal(newBST)


# Delete BST
print(deleteBST(newBST))
levelOrderTraversal(newBST)

