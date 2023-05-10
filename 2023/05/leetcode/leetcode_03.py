# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return len(s)
        else:
            max_len = 1
            for i in range(len(s)):
                for j in range(i+1, len(s)):
                    if s[j] in s[i:j]:
                        break
                    else:
                        max_len = max(max_len, j-i+1)
            return max_len
