class Solution:
    def helper(self, root: 'Node', res: List[int]) -> None:
        if root is None:
            return
        for child in root.children:
            self.helper(child, res)
        res.append(root.val)

    def postorder(self, root: 'Node') -> List[int]:
        res = []
        self.helper(root, res)
        return res