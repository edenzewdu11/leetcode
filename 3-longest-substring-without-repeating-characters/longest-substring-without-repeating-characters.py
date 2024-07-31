class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = set()
        i = 0
        max_length = 0
        for j in range(len(s)):
            while s[j] in char:
                char.remove(s[i])
                i += 1
            char.add(s[j])
            max_length = max(max_length, j - i + 1)
    
        return max_length

        