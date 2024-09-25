class TreeNode:
    def __init__(self, data, children = []) -> None:
        self.data = data
        self.children = children
    
    def addChild(self, treeNode):
        self.children.append(treeNode)

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"

        for child in self.children:
            ret += child.__str__(level + 1)
        
        return ret

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
tree.addChild(hot)
tree.addChild(cold)

tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
fanta = TreeNode('Fanta', [])
cola = TreeNode('Cola', [])

cold.addChild(cola)
cold.addChild(fanta)
hot.addChild(tea)
hot.addChild(coffee)
print(tree)