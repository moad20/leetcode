class Solution(object):
    def summaryRanges(self, nums):
        if len(nums) == 0:
            return []
        k = []
        i = 0
        while i <= len(nums)-1:
            j = i
            r = []
            while j <= len(nums)-1:
                if nums[j]+1 in nums:
                    r.append(nums[j])
                    j += 1
                else:
                    r.append(nums[j])
                    j += 1
                    break
            if len(r) != 1:
                k.append(str(r[0])+'->'+str(r[-1]))
            else:
                k.append(str(r[0]))
            i = j
        return k