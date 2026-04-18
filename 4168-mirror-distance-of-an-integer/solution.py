class Solution:
    def mirrorDistance(self, n: int) -> int:
        original=n
        reverse_d=0
        while n>0:
            ld=n%10
            reverse_d=reverse_d*10+ld
            n//=10
        return abs(original-reverse_d)
