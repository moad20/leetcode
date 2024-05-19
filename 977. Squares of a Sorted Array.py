class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqlist = []
        for i in range(len(nums)):
            sqlist.append(nums[i] * nums[i])
        sqlist.sort()
        return sqlist