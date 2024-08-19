class Solution(object):
    def repeatedSubstringPattern(self, s):
        concatenated = (s + s)[1:-1]
        return s in concatenated
        