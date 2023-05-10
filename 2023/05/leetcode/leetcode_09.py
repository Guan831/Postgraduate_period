# Given an integer x, return true if x is a  palindrome , and false otherwise.
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x = str(x)
            return x == x[::-1]
