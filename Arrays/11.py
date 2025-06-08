274. H-Index
Optimal Solution (Sort + Count)
class Solution(object):
    def hIndex(self, citations):
        # Step 1: Sort the citations in descending order
        # This helps us to easily find how many papers have at least i citations
        citations.sort(reverse=True)

        h = 0  # Initialize h-index

        # Step 2: Iterate over the sorted list
        for i, c in enumerate(citations):
            # i is the paper index (starting from 0), so i + 1 is the number of papers considered
            # Check if the current paper has at least (i + 1) citations
            if c >= i + 1:
                h += 1  # Increase h-index if condition is satisfied
            else:
                break  # As soon as we find a paper with less than (i + 1) citations, break

        # Step 3: Return the final h-index
        return h
t-O(nlogn)
s-O(1)

Counting Sort Approach
class Solution(object):
    def hIndex(self, citations):
        n = len(citations)
        count = [0] * (n + 1)
        
        # Count citations, cap anything greater than n
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        total = 0
        for i in range(n, -1, -1):
            total += count[i]
            if total >= i:
                return i
        return 0
t-O(n)	
s-O(n)