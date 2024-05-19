class Solution:
    def preOrder(self,root,answerList):
        if root == None:
            return answerList
        else:
            answerList.append(root.val)
            self.preOrder(root.left, answerList)
            self.preOrder(root.right, answerList)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answerList = []
        self.preOrder(root, answerList)

        return answerList