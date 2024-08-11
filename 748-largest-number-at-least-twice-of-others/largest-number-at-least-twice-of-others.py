class Solution(object):
    def dominantIndex(self, nums):
        max_val = max(nums)
        max_idx = nums.index(max_val)
        for n in nums:
            if n != max_val and max_val < 2 * n:
                return -1
            
        return max_idx

        