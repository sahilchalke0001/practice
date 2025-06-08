 14: Longest Common Prefix 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # Loop over characters of the first string
        for i in range(len(strs[0])):
            char = strs[0][i]

            for s in strs[1:]:
                # If i is out of bounds or characters don't match
                if i >= len(s) or s[i] != char:
                    return strs[0][:i]

        return strs[0]  # All characters matched
Time and Space Complexity:
Time Complexity: O(n * m)
→ n: number of strings, m: average length of strings

Space Complexity: O(1)
→ Just comparing, no extra data structures used