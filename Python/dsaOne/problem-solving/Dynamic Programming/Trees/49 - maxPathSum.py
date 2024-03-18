
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


def maxPathSum(rootNode, res):
    if rootNode is None:
        return 0
    
    l = maxPathSum(rootNode.leftChild, res)
    r = maxPathSum(rootNode.rightChild, res)

    temp = max(rootNode.data + max(l, r), rootNode.data)
    ans = max(temp, rootNode.data + l + r)
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

result = maxPathSum(newBST, -float('inf'))
print(result)

