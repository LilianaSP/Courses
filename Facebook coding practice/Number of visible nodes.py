#Number of Visible Nodes
#There is a binary tree with N nodes. You are viewing the tree from its left side and can see only the leftmost nodes at each level. Return the number of visible nodes.
#Note: You can see only the leftmost nodes, but that doesn't mean they have to be left nodes. The leftmost node at a level could be a right node.

#Example
#            8  <------ root
#           / \
#         3    10
#        / \     \
#       1   6     14
#          / \    /
#         4   7  13            
#output = 4

import math
# Add any extra import statements you may need here


class TreeNode: 
  def __init__(self,key): 
    self.left = None
    self.right = None
    self.val = key 

# Add any helper functions you may need here


def visible_nodes(root):
  # Write your code here
  if not root:
    return 0
  return 1 + max(visible_nodes(root.left), visible_nodes(root.right))
  