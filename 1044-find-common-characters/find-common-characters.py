class Solution(object):
    def commonChars(self, words):
        def count_chars(word):
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1
            return count
        
        common_count = count_chars(words[0])
        
        for word in words[1:]:
            current_count = count_chars(word)
            for char in common_count.keys():
                if char in current_count:
                    common_count[char] = min(common_count[char], current_count[char])
                else:
                    common_count[char] = 0
        
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result


        