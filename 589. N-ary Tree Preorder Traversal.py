class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        def function(root):
            if not root:
                return []
            answer.append(root.val)
            for child in root.children:
                function(child)
            return answer
        return function(root)