class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minSoFar = float('inf')
        prev = float('-inf')

        def recur(node):
            nonlocal minSoFar
            nonlocal prev
            
            if not node:
                return 
            
            recur(node.left)
            minSoFar = min(minSoFar, node.val - prev)
            prev = node.val
            recur(node.right)

        recur(root)
        return minSoFar