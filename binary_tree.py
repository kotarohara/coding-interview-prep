class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, node):
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while True:
                if node.value < current_node.value:
                    if current_node.left is None:
                        current_node.left = node
                        return
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = node
                        return
                    else:
                        current_node = current_node.right

    def _visit(self, node):
        return [node.value]

    def _iterate(self, node):
        ret = []
        if node.left:
            ret += self._iterate(node.left)
        ret += self._visit(node)
        if node.right:
            ret += self._iterate(node.right)
        return ret

    def traverse(self):
        for value in self._iterate(self.root):
            print value


if __name__ == "__main__":
    tree = Tree()
    values = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]

    # values = [4, 2, 1, 3, 6, 5, 7]
    for value in values:
        tree.add(Node(value))

    tree.traverse()
