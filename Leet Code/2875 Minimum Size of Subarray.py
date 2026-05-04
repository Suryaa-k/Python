from collections import deque

class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        full_cycles = target // total
        remainder = target % total
        base = full_cycles * n

        if remainder == 0:
            return base
        doubled = nums + nums
        min_window = float('inf')
        s = 0
        left = 0

        for right in range(len(doubled)):
            s += doubled[right]
            while s > remainder:
                s -= doubled[left]
                left += 1
            if s == remainder:
                min_window = min(min_window, right - left + 1)

        if min_window == float('inf'):
            return -1

        return base + min_window