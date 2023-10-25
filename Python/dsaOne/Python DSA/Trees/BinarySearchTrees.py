class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class SingleLinkedList:
    def __init__(self):
        self.root = None

    def insertion(self, val):
        newNode = Node(val)

        if(not self.root):
            self.root = newNode
            return self
        else:
            curr = self.root
            while(True):
                if(val == curr.val):
                    return None
                if(val < curr.val):
                    if(curr.left == None):
                        curr.left = newNode
                        return self
                    else:
                        curr = curr.left
                elif(val > curr.val):
                    if(curr.right == None):
                        curr.right = newNode
                        return self
                    else:
                        curr = curr.right
                    



tree = SingleLinkedList()
tree.insertion(10)
tree.insertion(5)
tree.insertion(2)
tree.insertion(12)
tree.insertion(15)
tree.insertion(11)
tree.insertion(11)

print(tree.root.val)
print(tree.root.left.val)
print(tree.root.left.left.val)
print(tree.root.right.val)
print(tree.root.right.right.val)
print(tree.root.right.left.val)
#tree.root.left = Node(5)
#tree.root.right = Node(15)
#tree.root.left.left = Node(4)
#print(tree.root.val)