class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
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
                        node.parent = current_node
                        return
                    else:
                        current_node = current_node.left

                else:
                    if current_node.right is None:
                        current_node.right = node
                        node.parent = current_node
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

    def find_lesser_and_greater(self, value):
        if self.root is None:
            return None
        else:
            lesser = self._find_lesser_node(value)
            greater = self._find_greater_node(value)

            if lesser:
                lesser = lesser.value
            else:
                lesser = None

            if greater:
                greater = greater.value
            else:
                greater = None
            return lesser, greater

    def _find_lesser_node(self, value):
        """
             4
           /   \
          2     6
         / \   / \
        1   3 5   7
        """
        current_node = self.root
        while True:
            if current_node is None:
                return None
            elif current_node.value < value:
                if current_node.right:
                    if current_node.right.value < value:
                        current_node = current_node.right
                    elif current_node.right.left and current_node.right.left.value < value:
                        current_node = current_node.right.left
                    else:
                        return current_node
                else:
                    return current_node
            else:
                current_node = current_node.left


    def _find_greater_node(self, value):
        current_node = self.root
        while True:
            if current_node is None:
                return None
            elif current_node.value > value:
                if current_node.left:
                    if current_node.left.value > value:
                        current_node = current_node.left
                    elif current_node.left.right and current_node.left.right.value > value:
                        current_node = current_node.left.right
                    else:
                        return current_node
                else:
                    return current_node
            else:
                current_node = current_node.right


if __name__ == "__main__":
    tree = Tree()
    # values = [21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40]

    values = [4, 2, 1, 3, 6, 5, 7]
    for value in values:
        tree.add(Node(value))

    print tree.find_lesser_and_greater(8)
