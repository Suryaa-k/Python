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
        good = 0

        rotate = {0: 0, 1: 1, 2: 5, 5: 2, 6: 9, 8: 8, 9: 6}

        for num in range(1, n + 1):
            temp = num
            rotated = 0
            place = 1
            valid = True
            changed = False

            while temp > 0:
                digit = temp % 10

                if digit not in rotate:
                    valid = False
                    break

                if rotate[digit] != digit:
                    changed = True

                rotated = rotate[digit] * place + rotated
                place *= 10
                temp //= 10

            if valid and changed:
                good += 1

        return good