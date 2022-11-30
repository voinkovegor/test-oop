class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj):
        if self.root is None:
            self.root = obj

        s, p, flag_find = self.__find(self.root, None, obj.data)

        if not flag_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for i in v:
                print(i.data, end=' ')
                if i.left:
                    vn += [i.left]
                if i.right:
                    vn += [i.right]
            print()
            v = vn


    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    def __del_one_child(self, s, p):
        if s.left is None:
            temp = s.right
        else:
            temp = s.left
        if s == p.left:
            p.left = temp
        elif s == p.right:
             p.right = temp

    def find_smallest(self, node):
        if node.left is None:
            return node
        self.find_smallest(node.left)

    def __del_two_childs(self, s, p):
        smallest_right = self.find_smallest(s.right)
        self.del_node(self.find_smallest(s.right))
        if s == p.left:
            p.left.data = smallest_right.data
        elif s == p.right:
            p.right.data = smallest_right.data

    def del_node(self, value):

        s, p, flag_find = self.__find(self.root, None, value)

        if flag_find == False:
            return None

        if s.left == None and s.right == None:
            self.__del_leaf(s, p)

        elif s.left == None or s.right == None:
            self.__del_one_child(s, p)

        else:
            self.__del_two_childs(s, p)


l = [1, 5, 4, 2, 8]

t = Tree()
for i in l:
    t.append(Node(i))

t.del_node(5)
t.show_wide_tree(t.root)
