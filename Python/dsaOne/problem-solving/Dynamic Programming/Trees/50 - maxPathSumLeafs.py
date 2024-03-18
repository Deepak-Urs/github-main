
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


def maxPathSumLeafs(rootNode, res):
    if rootNode is None:
        return 0
    
    l = maxPathSumLeafs(rootNode.leftChild, res)
    r = maxPathSumLeafs(rootNode.rightChild, res)

    temp = max(l, r) + rootNode.data
    if rootNode.leftChild is None and rootNode.rightChild is None:
        temp = max(temp, rootNode.data)
    ans = max(temp, rootNode.data + l + r)
    res = max(ans, res)

    return temp

newBST = BinarySearchTree(None)
insert(newBST, 10)
insert(newBST, 2)
insert(newBST, 1)
insert(newBST, 10)
insert(newBST, 3)
insert(newBST, 4)
insert(newBST, -25)

result = maxPathSumLeafs(newBST, -float('inf'))
print(result)

