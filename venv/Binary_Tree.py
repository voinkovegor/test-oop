class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if value == node.data:
            return node, parent, False

        if value < node.data:
            if node.left:
                return self.__find(node.left, parent, value)

        if value > node.data:
            if node.right:
                return self.__find(node.left, parent, value)


    def append(self, obj):
        if self.root is None:
            self.root = obj

