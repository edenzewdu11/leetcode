class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        mapping = {}
        
        for c, w in zip(pattern, words):
            if c in mapping:
                if mapping[c] != w:
                    return False
            else:
                if w in mapping.values():
                    return False
                mapping[c] = w
        
        return True


        