class Solution(object):
    def findErrorNums(self, nums):
        freq = [0] * len(nums)
        dup = -1
        missing = -1
        
        for num in nums:
            freq[num - 1] += 1
        
        for i in range(len(freq)):
            if freq[i] == 0:
                missing = i + 1
            elif freq[i] == 2:
                dup = i + 1
        
        return [dup, missing]

