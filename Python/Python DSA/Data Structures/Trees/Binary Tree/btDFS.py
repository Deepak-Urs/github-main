class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)

def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)


tN = TreeNode('Beverages')
leftChild = TreeNode('Cold')
rightChild = TreeNode('Hot')
tN.leftChild =  leftChild
tN.rightChild = rightChild

print('--preOrder--')
preOrder(tN)
print('-----')
print('--inOrder--')
inOrder(tN)
print('-----')
print('--postOrder--')
postOrder(tN)
print('-----')