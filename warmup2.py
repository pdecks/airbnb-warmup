"""Element Present in Tree?"""
# element present in BST
"""
class BSTreeNode:
    def __init__(self, node_value):
        self.value = node_value
        self.left = self.right = None
"""

def isPresent (root,val):
    # write your code here
    # return 1 or 0 depending on whether the element is present in the tree or not
    curr_node = root
    while curr_node:
        if curr_node.value == val:
            return 1
        elif curr_node.value < val and curr_node.right: # move right
            curr_node = curr_node.right
        elif curr_node.value > val and curr_node.left: # move left
            curr_node = curr_node.left
        else:
            return 0
    return 0