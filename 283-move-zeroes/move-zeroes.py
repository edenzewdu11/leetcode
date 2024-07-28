class Solution(object):
    def moveZeroes(self, nums):
        
        non_zero_elements = [num for num in nums if num != 0]
        
        
        zero_count = len(nums) - len(non_zero_elements)
        
       
        result = non_zero_elements + [0] * zero_count
        
       
        for i in range(len(nums)):
            nums[i] = result[i]
        
        return nums
