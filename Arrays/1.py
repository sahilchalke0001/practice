# 1929. Concatenation of Array - Explanation

# Input: nums = [1,4,1,2]

# Output: [1,4,1,2,1,4,1,2]

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans


         nums+nums #option 2

T-O(n^2)
S-O(n)