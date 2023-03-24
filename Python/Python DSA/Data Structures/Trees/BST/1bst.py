import QueueLinkedList as queue

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNodeBT(rootNode, nodeValue):
    if not rootNode:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNodeBT(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNodeBT(rootNode.rightChild, nodeValue)
    return "The node value has been successfully inserted"

def preOrderTraversalBST(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversalBST(rootNode.leftChild)
    preOrderTraversalBST(rootNode.rightChild)

def inOrderTraversalBST(rootNode):
    if not rootNode:
        return
    inOrderTraversalBST(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversalBST(rootNode.rightChild)

def postOrderTraversalBST(rootNode):
    if not rootNode:
        return
    postOrderTraversalBST(rootNode.leftChild)
    postOrderTraversalBST(rootNode.rightChild)
    print(rootNode.data)

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

def searchBST(rootNode, nodeValue):
    # stops when the value is not there
    if rootNode.data == nodeValue:
        print("Value found")
    elif nodeValue < rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            print("Value found")
        else:
            searchBST(rootNode.leftChild, nodeValue)
    elif nodeValue > rootNode.data:
        if nodeValue == rootNode.leftChild.data:
            print("Value found")
        else:
            searchBST(rootNode.rightChild, nodeValue)

def minValNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(rootNode, nodeValue):
    # revisit this concept
    if not rootNode:
        return "BST Empty"
    else:
        if nodeValue < rootNode.data:
            rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = deleteNode(rootNode.rightChild)
        else:
            if rootNode.leftChild is None:
                temp = rootNode.rightChild
                rootNode = None
                return temp

            if rootNode.rightChild is None:
                temp = rootNode.leftChild
                rootNode = None
                return temp

            temp = minValNode(rootNode.leftChild)
            rootNode.data = temp.data
            rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)

        return rootNode

def deleteBST(rootNode):
    if not rootNode:
        return "BST Empty"
    else:
        rootNode.leftChild = None
        rootNode.rightChild = None
        rootNode.data = None
        return "The BST is deleted successfully"



bst = BSTNode(70)
print(insertNodeBT(bst, 60))
print(insertNodeBT(bst, 80))
#print(bst.data)
#print(bst.leftChild.data)
#print(bst.rightChild.data)

#print('preOrderTraversalBST----')
#print(preOrderTraversalBST(bst))

#print('inOrderTraversalBST----')
#print(inOrderTraversalBST(bst))

#print('postOrderTraversalBST----')
#print(postOrderTraversalBST(bst))

#print('levelOrderTraversal----')
#print(levelOrderTraversal(bst))


print('searchBST----')
print(searchBST(bst, 60))

print('deleteNode----')
print(deleteNode(bst, 60))

print('levelOrderTraversal----')
print(levelOrderTraversal(bst))

print('deleteBST----')
print(deleteBST(bst))

print('levelOrderTraversal----')
print(levelOrderTraversal(bst))

