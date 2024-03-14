import sys

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


def diameterBinaryTree(rootNode, res):
    if rootNode is None:
        return 0
    
    l = diameterBinaryTree(rootNode.leftChild, res)
    r = diameterBinaryTree(rootNode.rightChild, res)

    temp = 1 + max(l,r)
    ans = max(temp, 1+l+r)
    res = max(ans, res)

    return temp

newBST = BinarySearchTree(None)
insert(newBST, 70)
insert(newBST, 50)
insert(newBST, 90)
insert(newBST, 30)
insert(newBST, 60)
insert(newBST, 80)
insert(newBST, 100)
insert(newBST, 20)
insert(newBST, 40)

result = diameterBinaryTree(newBST, -1)
print(result)

