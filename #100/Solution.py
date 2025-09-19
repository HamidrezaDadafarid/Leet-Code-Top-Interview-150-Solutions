# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Helper function to compare two trees
        def same(p, q):
            # Both nodes are None, trees are the same up to this point
            if not p and not q:
                return True
            # One node is None and the other is not, trees are not the same
            elif (not p and q) or (p and not q):
                return False
            # Node values are different, trees are not the same
            elif p.val != q.val:
                return False

            # Recursively check left and right subtrees
            return same(p.left, q.left) and same(p.right, q.right)

        return same(p, q)

# Time Complexity: O(N), where N is the total number of nodes in the tree. This is because we visit each node exactly once.
# Space Complexity: O(H), where H is the height of the tree. This is the space used by the call stack during the recursion.
