class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n=len(positions)

        robots=sorted([(positions[i],healths[i],directions[i],i) for i in range(n)])
        stack=[]
        alive=[True]*n

        health=healths[:]

        for pos,h,d,idx in robots:
            if d=='R':
                stack.append(idx)
            else:
                while stack:
                    top=stack[-1]
                    
                    if not alive[top]:
                        stack.pop()
                        continue

                    if health[top]>health[idx]:
                        health[top]-=1
                        alive[idx]=False

                        break

                    elif health[top]<health[idx]:
                        health[idx]-=1
                        alive[top]=False
                        stack.pop()

                    else:
                        alive[top]=False
                        alive[idx]=False
                        stack.pop()
                        break

        result=[]
        for i in range(n):
            if alive[i]:
                result.append(health[i])


        return result
        
