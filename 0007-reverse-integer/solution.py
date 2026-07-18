class Solution:
    def reverse(self, x: int) -> int:
        negative=False
        n=0
        if x<0:
            negative=True
            x=-x

        while x>0:
            ld=x%10
            n=n*10+ld
            x=x//10
        
        if negative==True:
            n=n*(-1)
        if n < -2147483648 or n > 2147483647:
            return 0
           

        return n
        
