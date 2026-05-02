# 788. Rotated Digits
#
# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different
# from x. Each digit must be rotated - we cannot choose to leave it alone.A number is valid if each digit remains a digit
# after rotation. For example:
# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].

class Solution:
    def rotatedDigits(self, n: int) -> int:
        digits = list(map(int, str(n)))

        from functools import lru_cache

        invalid = {3, 4, 7}
        diff = {2, 5, 6, 9}

        @lru_cache(maxsize=None)
        def dp(pos, tight, changed):
            if pos == len(digits):
                return 1 if changed else 0

            limit = digits[pos] if tight else 9
            result = 0

            for d in range(0, limit + 1):
                if d in invalid:
                    continue
                result += dp(
                    pos + 1,
                    tight and d == limit,
                    changed or d in diff
                )
            return result

        return dp(0, True, False)