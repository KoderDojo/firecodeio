"""
Given a binary search tree and an integer k, implement
a method to find and return the kth smallest node.
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

    # Helper Method
    def size(self, root):
        if root == None:
            return 0
        else:
            return (self.size(root.left_child) + 1 + self.size(root.right_child))

    def find_kth_smallest(self, root, k):
        if root is None:
            return None

        stack, count = [root], 0
        visited = set()

        while len(stack) > 0:
            if stack[-1].left_child is not None and stack[-1].left_child not in visited:
                visited.add(stack[-1].left_child)
                stack.append(stack[-1].left_child)
                continue

            node = stack.pop()
            count += 1
            if count == k:
                return node

            if node.right_child is not None and node.right_child not in visited:
                stack.append(node.right_child)
                visited.add(node.right_child)

root_node = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4, None, TreeNode(5)))
b = BinaryTree(root_node)
print(b.find_kth_smallest(root_node, 5))
