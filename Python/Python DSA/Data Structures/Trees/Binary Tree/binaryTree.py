from dataclasses import dataclass


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftNode = None
        self.rightNode = None

newBT = TreeNode('Drinks')