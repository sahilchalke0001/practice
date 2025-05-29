# 242. Valid Anagram
# Input: s = "racecar", t = "carrace"

# Output: true

from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        return Counter(s)==Counter(t)

T-O(n)
S-O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)

T-O(nlogn + mlogm)
S-O(n+m)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

T-O(n)
SO(n)