# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# time complexity O(n)
# space complexity O(h) h is the height of binary tree
class RecursiveSolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            return [ root.val ] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

class IterativeSolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:        
        res = []
        if not root:
            return res
        stack = [root]
        while(stack):
            cur = stack.pop()
            res.append(cur.val)
            if(cur.right):
                stack.append(cur.right)
            if(cur.left):
                stack.append(cur.left)
        return res

