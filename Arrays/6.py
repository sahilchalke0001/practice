# 49. Group Anagrams (meduium)
# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)#list cannot be keys thats why tuple
        return res.values()

# You're referring to this part of the code:
# ```python
# res[tuple(count)].append(s)
# ```
# and
# ```python
# return list(res.values())
# ```
# ---
# ### ✅ Why is a `tuple(count)` used as a **key**?
# #### ➤ Reason:
# * In Python, **lists are not hashable** (they can't be used as dictionary keys).
# * **Tuples are hashable**, so they **can** be used as keys in a `dict` or `defaultdict`.
# 🔹 `count` is a list of 26 integers (representing the frequency of letters `a` to `z` in the string).
# * For example, for `"eat"`, count might be like:
#   `[1, 0, 0, 0, 1, 0, 0, ..., 1, ..., 0]` → (1 at 'e', 'a', 't')
# ✅ So `tuple(count)` converts that list into an immutable, hashable form to use as a **key**.
# #### Why it works:
# * All anagrams have the **same character frequency**, so they will share the same `tuple(count)` key.
# * This groups anagrams together in the dictionary.
# ---
# ### ✅ Why is `list(res.values())` returned?
# `res` is a dictionary of the form:
# ```python
# {
#   (1, 0, ..., 1): ['eat', 'tea', 'ate'],
#   (1, 1, ..., 0): ['bat'],
#   ...
# }
# ```
# * `res.values()` gives you just the **lists of grouped anagrams** (without the tuple keys).
# * `list(res.values())` converts the dictionary values view into an actual list.
# ---
# ### 🔄 Summary:
# | Expression                    | Purpose                                                       |
# | ----------------------------- | ------------------------------------------------------------- |
# | `tuple(count)`                | Make `count` hashable to use as a dictionary key              |
# | `res[tuple(count)].append(s)` | Add the string `s` to the group matching its letter frequency |
# | `list(res.values())`          | Return just the grouped anagram lists (ignoring keys)         |
# ---
# ### 🔧 Example:
# Input:
# ```python
# ["eat", "tea", "tan", "ate", "nat", "bat"]
# ```
# Output:
# ```python
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
# ```
# Let me know if you’d like a dry run or visualization for better understanding!
