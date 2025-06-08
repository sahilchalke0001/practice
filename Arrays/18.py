12. Integer to Roman
class Solution(object):
    def intToRoman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]

        roman = ""
        i = 0

        while num > 0:
            # Subtract value as many times as possible
            while num >= val[i]:
                roman += syms[i]
                num -= val[i]
            i += 1

        return roman
Time and Space Complexity:
Time Complexity: O(1) — maximum 13 symbols processed due to greedy logic and fixed value set.

Space Complexity: O(1) — output string is bounded by 15 characters max (for 3888: "MMMDCCCLXXXVIII").