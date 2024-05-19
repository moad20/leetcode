class Solution(object):
    def rangeSumBST(self, root, low, high):
        sum_val = 0
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if low <= root.val <= high:
                sum_val += root.val

            root = root.right

        return sum_val