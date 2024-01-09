from collections import Counter, defaultdict

class Solution:
    def allItemGreaterOrEqualThanGiven(self, required_characters, current_characters):
        for key in required_characters:
            if current_characters[key] < required_characters[key]:
                return False
        return True

        pass
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        required_characters = Counter(t)
        current_characters = defaultdict(int)
        t_substring_index = []
        left = -1
        right = 0
        min_length = len(s)+1
        min_left, min_right = 0, 0

        while left < len(s) and right < len(s):
            if s[right] in required_characters:
                current_characters[s[right]]+=1
                t_substring_index.append(right)
            right+=1
            
            while self.allItemGreaterOrEqualThanGiven(required_characters, current_characters) and left < len(s):
                current_window = right-left
                if current_window < min_length and required_characters == current_characters:
                    min_left, min_right = left, right
                    min_length = min(min_length, current_window)
                
                if len(t_substring_index) > 0:
                    if left >= 0:
                        current_characters[s[left]]-=1
                    left = t_substring_index.pop(0)
                else:
                    left+=1
                
        
        return(s[min_left:min_right])



dd = Solution()
print(dd.minWindow("ab", "a")) # "a"
print(dd.minWindow("ADOBECODEBANC", "ABC"))
print(dd.minWindow("a", "a"))
print(dd.minWindow("a", "aa"))