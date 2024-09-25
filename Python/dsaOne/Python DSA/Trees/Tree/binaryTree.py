class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftC = None
        self.rightC = None
    
newTree = TreeNode('Drinks') #O(1), O(1)
hot = TreeNode('Hot')
cold = TreeNode('Cold')

tea = TreeNode('Tea')
coffee = TreeNode('Coffee')
cola = TreeNode('Cola')
fanta = TreeNode('Fanta')


hot.leftC = tea
hot.rightC = coffee
cold.leftC = cola
cold.rightC = fanta

newTree.leftC = hot
newTree.rightC = cold

def preOrderTraversal(rootNode): # O(n), O(n)
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftC)
    preOrderTraversal(rootNode.rightC)

def inOrderTraversal(rootNode): # O(n), O(n)
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftC)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightC)

def postOrderTraversal(rootNode): # O(n), O(n)
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftC)
    postOrderTraversal(rootNode.rightC)
    print(rootNode.data)




#preOrderTraversal(newTree)
#inOrderTraversal(newTree)
postOrderTraversal(newTree)


