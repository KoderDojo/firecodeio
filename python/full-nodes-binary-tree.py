class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    # Required collection modules have already been imported.
    def number_of_full_nodes(self, root):
        if root is None:
            return 0

        if root.left_child is not None and root.right_child is not None:
            return 1 + self.number_of_full_nodes(root.left_child) +\
                   self.number_of_full_nodes(root.right_child)
        elif root.left_child is not None:
            return self.number_of_full_nodes(root.left_child)
        else:
            return self.number_of_full_nodes(root.right_child)
