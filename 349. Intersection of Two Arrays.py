class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        intersection_set = nums1.intersection(nums2)
        intersection_list = list(intersection_set)
        return intersection_list
        