class Solution(object):
    def majorityElement(self, nums):
        n=len(nums)
        m={}
        for num in nums:
            if num not in m:
                m[num]=1
            else:
                m[num]+=1
        n=n//2
        for key,value in m.items():
            if value>n:
                return key


       
        