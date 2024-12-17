class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        stack =[]
        minval = root.val
        secondmin = float('inf')
        cur = root
        flag = False
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if minval < cur.val < secondmin:
                secondmin = cur.val
                flag = True
            cur = cur.right
        
        return secondmin if flag else -1