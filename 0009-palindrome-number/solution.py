class Solution:
    def isPalindrome(self, n: int) -> bool:
        revnum=self.check(n)
        if(n==revnum):
            return True
        else:
            return False
    def check(self,n):
        revnum=0
        while n>0:
            revnum=revnum*10+n%10
            n=n//10
        return revnum

