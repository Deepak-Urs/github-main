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
levelOrderTraversal(newBST)


