class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(n):
            if i==0:
                if nums[0]!=nums[1]:
                    return  nums[0]
            elif i==n-1:
                if nums[n-1]!=nums[n-2]:
                    return nums[n-1]
            else: 
                if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                    return nums[i]

        return -1
            
