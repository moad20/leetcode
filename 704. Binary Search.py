class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Finding the mid using floor division
            mid = low + ((high - low) // 2)

            # Target value is present at the middle of the array
            if nums[mid] == target:
                return mid

            # Target value is present in the low subarray
            elif target < nums[mid]:
                high = mid - 1

            # Target value is present in the high subarray
            elif target > nums[mid]:
                low = mid + 1

        # Target value is not present in the array
        return -1