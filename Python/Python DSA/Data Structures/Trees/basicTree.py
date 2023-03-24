from tokenize import Number


class TreeNode:
    def __init__(self, data: Number, children= []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
coffee = TreeNode('Coffee', [])
tea = TreeNode('tea', [])
fanta = TreeNode('fanta', [])

tree.addChild(cold)
tree.addChild(hot)
cold.addChild(cola)
hot.addChild(coffee)
cold.addChild(fanta)
hot.addChild(tea)

print(tree)