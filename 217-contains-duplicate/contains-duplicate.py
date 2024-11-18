class Solution(object):
    def containsDuplicate(self, arr):
        m= {}
        for value in arr:
            if value in m:
                return True
            m[value] = 1
        return False
