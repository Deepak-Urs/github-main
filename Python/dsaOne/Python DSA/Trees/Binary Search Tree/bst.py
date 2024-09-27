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
def levelOrderTraversal(rootNode):
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
    
newBST = BSTNode(None)      # O(1), O(1)
insertNodeBST(newBST, 70)
insertNodeBST(newBST, 50)
insertNodeBST(newBST, 80)
insertNodeBST(newBST, 30)
insertNodeBST(newBST, 45)
insertNodeBST(newBST, 75)
insertNodeBST(newBST, 90)

print(newBST.data)
print('newBST.leftChild.data', newBST.leftChild.data)
print('newBST.rightChild.data', newBST.rightChild.data)

# DFS
#print('preOrderTraversal\n')
#preOrderTraversal( newBST)
#print('inOrderTraversal\n')
#inOrderTraversal(newBST)
#print('postOrderTraversal\n')
#postOrderTraversal(newBST)

# BFS
levelOrderTraversal(newBST)