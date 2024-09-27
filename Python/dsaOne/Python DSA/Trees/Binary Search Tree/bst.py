# creation of BST
class BSTNode:
    def __init__(self, data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBST = BSTNode(None)  # O(1), O(1)