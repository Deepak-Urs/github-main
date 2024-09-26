import QueueLinkedList as queue
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

def levelOrderTraversal(rootNode): # O(n), O(n)
    if not rootNode:
        return
    
    customQ = queue.Queue()
    customQ.enqueue(rootNode)

    while not customQ.isEmpty():
        root = customQ.dequeue()
        print(root.value.data)

        if root.value.leftC is not None:
            customQ.enqueue(root.value.leftC)
        
        if root.value.rightC is not None:
            customQ.enqueue(root.value.rightC)


def searchBT(rootNode, val): # O(n), O(n)
    if not rootNode:
        return "BT is empty!"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.data == val:
                print("Search Success!")
                return 
            
            if root.value.leftC is not None:
                customQ.enqueue(root.value.leftC)

            if root.value.rightC is not None:
                customQ.enqueue(root.value.rightC)
        
        print("Search Failure")
        return 
    
def insertNodeBT(rootNode, val): # O(n), O(n)
    newNode = TreeNode(val)
    if not rootNode:
        return newNode
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.leftC is not None:
                customQ.enqueue(root.value.leftC)
            else:
                root.value.leftC = newNode
                return "Insertion Success"
            
            if root.value.rightC is not None:
                customQ.enqueue(root.value.rightC)
            else:
                root.value.rightC = newNode
                return "Insertion Success"

def findDeepestNode(rootNode) -> TreeNode:
    if not rootNode:
        return "BT empty!"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.leftC is not None:
                customQ.enqueue(root.value.leftC)
            
            if root.value.rightC is not None:
                customQ.enqueue(root.value.rightC)
        
        deepestNode = root.value
        print('deepestNode data', deepestNode.data)
        return deepestNode

def deleteDeepestNode(rootNode, dNode) -> None:
    if not rootNode:
        return "BT Empty!"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()
            
            if root.value == dNode:
                root.value = None
                return
            
            if root.value.leftC:
                if root.value.leftC is dNode:
                    root.value.leftC = None
                    return
                else:
                    customQ.enqueue(root.value.leftC)
            
            if root.value.rightC:
                if root.value.rightC:
                    root.value.rightC = None
                    return
                else:
                    customQ.enqueue(root.value.rightC)
        

def deleteNodeBT(rootNode, node): # O(n), O(n)
    print('I/P for deleteNodeBT', node)
    if not rootNode:
        return "BT is empty"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.data == node:
                dNode = findDeepestNode(rootNode)
                print('dNode seen', dNode.data)
                # need a check here for leaf and non leaf node deletions
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Node deletion success!"
            
            if root.value.leftC is not None:
                customQ.enqueue(root.value.leftC)
            
            if root.value.rightC is not None:
                customQ.enqueue(root.value.rightC)
        
        return "Failed to delete the node"

            
def deleteEntireBT(rootNode): # O(1)
    if not rootNode:
        return "BT Empty!"
    else:
        rootNode.data = None
        rootNode.leftC = None
        rootNode.rightC = None


# DFS
#preOrderTraversal(newTree)
#inOrderTraversal(newTree)
#postOrderTraversal(newTree)

# BFS
#levelOrderTraversal(newTree)
    
# Search
#searchBT(newTree, "Tea")
            
# Insert
#insertNodeBT(newTree, "Green Tea")
#levelOrderTraversal(newTree)
    
# Delete
#print(deleteNodeBT(newTree, "Tea"))
#levelOrderTraversal(newTree)
        
deleteEntireBT(newTree)
levelOrderTraversal(newTree)