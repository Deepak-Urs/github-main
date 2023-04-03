import QueueLinkedList as Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQ = Queue.Queue()
        customQ.enqueue(rootNode)

        while not customQ.isEmpty():
            root = customQ.dequeue()

            print(root.value.data)
            if root.value.leftChild is not None:
                customQ.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQ.enqueue(root.value.rightChild)
            




newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
lCl = TreeNode("Coffee")
lCr = TreeNode("Tea")
rCl = TreeNode("Fanta")
rCr = TreeNode("Sprite")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = lCl
leftChild.rightChild = lCr
rightChild.leftChild = rCl
rightChild.rightChild = rCr

print("preOrderTraversal --")
preOrderTraversal(newBT)
print("\n")

print("inOrderTraversal --")
inOrderTraversal(newBT)
print("\n")

print("postOrderTraversal --")
postOrderTraversal(newBT)
print("\n")

print("levelOrderTraversal --")
levelOrderTraversal(newBT)
print("\n")
