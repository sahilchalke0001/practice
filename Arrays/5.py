# 14. Longest Common Prefix

# Input: strs = ["bat","bag","bank","band"]

# Output: "ba"

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i] 
        return res

Case	        Time Complexity	Space Complexity
Best Case	                 O(1)	         O(1)
Average/Worst	         O(N × M)	         O(M) 

# Summary of Steps:
# Initialize res as empty.
# Loop through character positions of the first string.
# For each character position i, check if all strings have the same character at that index.
# If any string ends early or has a mismatch, return current res.
# If all match, add character to res.
# Return final result.