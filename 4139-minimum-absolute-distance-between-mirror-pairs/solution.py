class Solution:
    def minMirrorPairDistance(self, nums: list[int]) -> int:
        last_seen = {}  
        min_dist = float('inf')

        for j, num in enumerate(nums):
            rev = self.reverse_num(num)

            if num in last_seen:
                min_dist = min(min_dist, j - last_seen[num])

            last_seen[rev] = j

        return -1 if min_dist == float('inf') else min_dist

    def reverse_num(self, x: int) -> int:
        rev = 0
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        return rev
