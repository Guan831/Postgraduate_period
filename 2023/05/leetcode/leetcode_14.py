# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            min_len = min([len(s) for s in strs])
            for i in range(min_len):
                for j in range(1, len(strs)):
                    if strs[j][i] != strs[j-1][i]:
                        return strs[0][:i]
            return strs[0][:min_len]
