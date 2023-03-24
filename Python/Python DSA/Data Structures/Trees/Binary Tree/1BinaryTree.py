import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

# creation of BT
newBT = TreeNode("Drinks")
lC = TreeNode("Hot")
rC = TreeNode("Cold")

lCl = TreeNode("Coffee")
lCr = TreeNode("Tea")
rCl = TreeNode("Fanta")
rCr = TreeNode("Pepsi")

newBT.leftChild = lC
newBT.rightChild = rC

lC.leftChild = lCl
lC.rightChild = lCr

rC.leftChild = rCl
rC.rightChild = rCr

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inorderTraversal(rootNode):
    if not rootNode:
        return
    else:
        inorderTraversal(rootNode.leftChild)
        print(rootNode.data)
        inorderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
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

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)

            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
        
        return "Value not found"

def insertNodeBinaryTree(rootNode, newNode): 
    if not rootNode:
        rootNode = newNode
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Insertion successfull!"

            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Insertion successfull!"


def getDeepestNode(rootNode):
    if not rootNode:
        return "BT is empty!"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            
        deepestNode = root.value

        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return "BT is empty"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()
            if root.value is dNode:
                root.value = None
                return
            
            if root.value.leftChild is dNode:
                root.value.leftChild = None
                return
            else:
                customQ.enqueue(root.value.leftChild)

            if root.value.rightChild is dNode:
                root.value.rightChild = None
                return
            else:
                customQ.enqueue(root.value.rightChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return "BT is empty"
    else:
        customQ = queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
        
        return "Failed to delete the expected value"

def deleteBT(rootNode):
    if not rootNode:
        return "BT is empty"
    else:
        rootNode.leftChild = None
        rootNode.rightChild = None
        rootNode.data = None
        return "The BT is sucecessfully deleted"


# preorder --
# n1,n2,n4,n9,n10,n5,n3,n6,n7

# inorder --
# n9,n4,n10,n2,n5,n1,n6,n3,n7

# postorder --
# n9,n10,n4,n5,n2,n6,n7,n3,n1

#levelorder/bfs
#n1,n2,n3,n4,n5,n6.n7,n8,n9,n10

#print('preOrderTraversal--')
#preOrderTraversal(newBT)

#print('inorderTraversal--')
#inorderTraversal(newBT)

#print('postOrderTraversal--')
#postOrderTraversal(newBT)

#print('levelOrderTraversal--')
#levelOrderTraversal(newBT)

#print('Search Operations --')
#print(searchBT(newBT, "Tea"))
#print(searchBT(newBT, "Teas"))

#newNode = TreeNode("Cola")
#newNode2 = TreeNode("Sprite")
#print('Insertion Operations --')
#print(insertNodeBinaryTree(newBT, newNode))
#print(insertNodeBinaryTree(newBT, newNode2))
#levelOrderTraversal(newBT)


#print('getDeepestNode Operations --')
#result = getDeepestNode(newBT)
#print(result.data)


#newNode = getDeepestNode(newBT)
#deleteDeepestNode(newBT, newNode)
#levelOrderTraversal(newBT)

#deleteNodeBT(newBT, 'Coffee')
#levelOrderTraversal(newBT)

deleteBT(newBT)
levelOrderTraversal(newBT)