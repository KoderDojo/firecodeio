"""
Given a binary tree, write a function to recursively traverse
it in the preorder manner. Mark a node as visited by adding
its data to the list - pre_ordered_list(defined globally
at the top of the editor).
"""
pre_ordered_list = []


class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def preorder(self):
        pre_ordered_list.append(self.data)
        if self.left_child is not None:
            self.left_child.preorder()
        if self.right_child is not None:
            self.right_child.preorder()

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data
