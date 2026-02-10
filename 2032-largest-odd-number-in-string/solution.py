class Solution:
    def largestOddNumber(self, s: str) -> str:
        ind=-1
        i=0
        for i in range(len(s)-1,-1,-1):
            if(int(s[i])%2==1):
                return s[:i + 1]
        return ""

