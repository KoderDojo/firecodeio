"""
Implement a method to insert a node into a
Binary Search Tree. Return the root of the
modified tree.
"""


class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' % self.data


class BinaryTree:
    def __init__(self, root_node=None):
        # Check out Use Me section to find out Node Structure
        self.root = root_node

    def insert(self, root, data):
        previous_node, current_node = None, root

        while current_node is not None:
            previous_node = current_node
            if data < current_node.data:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

        if previous_node is None:
            return TreeNode(data)

        if data < previous_node.data:
            previous_node.left_child = TreeNode(data)
        else:
            previous_node.right_child = TreeNode(data)

        return root

t = BinaryTree()
r = t.insert(None, 1)
r = t.insert(r, 2)
r = t.insert(r, 3)
r = t.insert(r, 4)
r = t.insert(r, 5)
r = t.insert(r, 6)
r = t.insert(r, 7)
print(r)
