class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class BinaryTreeDict:
    def __init__(self):
        self.root = None

    def insert(self, key, val):
        if not self.root:
            self.root = Node(key, val)
        else:
            self._insert(self.root, key, val)

    def _insert(self, node, key, val):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, val)
            else:
                self._insert(node.left, key, val)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, val)
            else:
                self._insert(node.right, key, val)
        else:
            node.val = val  # If the key already exists, update the value

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
