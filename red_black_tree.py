BLACK = 0
RED = 1


class RBNode(object):

    def __init__(self, value, color=RED):
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
        self.value = value


class RBTree(object):

    def __init__(self):
        self.root = None

    def rotate_left(self, node):
        temp_node = node.right
        node.right = temp_node.left
        temp_node.left = node

        temp_node.parent = node.parent
        node.parent = temp_node

    def rotate_right(self, node):
        temp_node = node.left
        node.left = temp_node.right
        temp_node.right = node

        temp_node.parent = node.parent
        node.parent = temp_node

    def search_place_to_insert(self, current_node, node):
        if current_node.value is None:
            return current_node

        elif node.value < current_node.value:
            return self.search_place_to_insert(current_node.left, node)
        else:
            return self.search_place_to_insert(current_node.right, node)

    def balance(self):
        pass

    def insert_node(self, node):
        target = self.search_place_to_insert(self.root, node)
        parent = target.parent
        node.parent = parent
        if parent.right == target:
            parent.right = node
        else:
            parent.left = node

        self.balance()

    def insert(self, value):
        node = RBNode(value)
        self.insert_node(node)
