class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m,n=len(coins),len(coins[0])
        INF=float('-inf')
        dp=[[INF]*3 for _ in range(n)]
        for i in range(m):
            new_dp=[[INF]*3 for _ in range(n)]

            for j in range(n):
                for k in range(3):
                    best=INF
                    
                    if i==0 and j==0:
                        best=0
                    else:

                        if i>0:
                            best=max(best,dp[j][k])

                        if j>0:
                            best=max(best,new_dp[j-1][k])

                    if best==INF:
                        continue

                    val=coins[i][j]
                    new_dp[j][k]=max(new_dp[j][k],best+val)

                    if val<0 and k>0:
                        best_k1=INF

                        if i==0 and j==0:
                            best_k1=0
                        else:
                            if i>0:
                                best_k1=max(best_k1,dp[j][k-1])

                            if j>0:
                                best_k1=max(best_k1,new_dp[j-1][k-1])

                        if best_k1!= INF:
                            new_dp[j][k]=max(new_dp[j][k],best_k1)

            dp=new_dp

        return max(dp[n-1])       


        
