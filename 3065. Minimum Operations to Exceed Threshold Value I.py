class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        left = 0
        
        for right in range(len(nums)):
            if nums[right]<k:
                nums[left] = nums[right]
                left +=1
        return left
            

    