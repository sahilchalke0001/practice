# 14. Longest Common Prefix

# Input: strs = ["bat","bag","bank","band"]

# Output: "ba"

def longestCommonPrefix(strs):
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]

T-O(N*M)
S-O(1)

