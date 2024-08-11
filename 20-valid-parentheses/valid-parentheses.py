class Solution(object):
    def isValid(self, s):
        m = {')': '(', '}': '{', ']': '['}
        stk = []
        
        for c in s:
            if c in m:
                top = stk.pop() if stk else '#'
                if m[c] != top:
                    return False
            else:
                stk.append(c)
        
        return not stk
