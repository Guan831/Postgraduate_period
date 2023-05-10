# Given a string s, return the longest  palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len, start = 0, 0
        for i in range(n):
            # 以 i 为中心向两边扩展，寻找最长回文子串
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            curr_len = max(len1, len2)
            if curr_len > max_len:
                max_len = curr_len
                start = i - (max_len - 1) // 2
        print(s[start:start+max_len])
        return s[start:start+max_len]

    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
        # 寻找以 (left, right) 为中心的最长回文子串
        n = len(s)
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
