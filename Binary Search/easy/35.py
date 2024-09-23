class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = -1
        r = len(nums)
        while r - l > 1:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m
        return r   
