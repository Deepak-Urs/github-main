import QueueLinkedList as queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

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
            
tN = TreeNode('Beverages')
leftKid = TreeNode('Cold')
rightKid = TreeNode('Hot')
lC = TreeNode('Fanta')
rC = TreeNode('Sprite')
lH = TreeNode('Tea')
rH = TreeNode('Coffee')
tN.leftChild =  leftKid
tN.rightChild = rightKid
leftKid.leftChild = lC
leftKid.rightChild = rC
rightKid.leftChild = lH
rightKid.rightChild = rH

print('LevelOrder result:')
levelOrderTraversal(tN)
