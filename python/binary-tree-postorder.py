"""
Given a binary tree, implement a method to populate
the list post_ordered_list with the data of the nodes
traversed in postorder, recursively.
"""

post_ordered_list = []


class BinaryTree:
    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def postorder(self):

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data