class TreeNode:
  def __init__(self, key):
    self.left = None
    self.right = None
    self.data = key

#   def __str__(self):
#     # preorder traversal
#     answer = str(self.key)
#     if self.left:
#       answer += str(self.left)
#     if self.right:
#       answer += str(self.right)
#     return answer

def largest_bst_subtree(root):
    if node is None:
        return None
    broot = TreeNode(root.data)
    if root.left:
        if root.left.data<root.data:
            broot.left = largest_bst_subtree(root.left)
        else:
            broot=None
            broot = largest_bst_subtree(root.left)
    if root.right:
        if root.right.data>root.data:
            broot.right = largest_bst_subtree(root.right)
        else:
            broot=None
            broot = largest_bst_subtree(root.right)
            #broot.right = TreeNode(root.right.data)
    return broot
def PreorderTraversal(node):
    print(node.data)
    if node.left:
        PreorderTraversal(node.left)
    if node.right:
        PreorderTraversal(node.right)              
  # Fill this in

#     5
#    / \
#   6   7
#  /   / \
# 2   4   9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
tree= largest_bst_subtree(node)
PreorderTraversal(tree)