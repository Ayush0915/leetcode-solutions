class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnts=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[cnts]=nums[i]
                cnts+=1
        for i in range(cnts,n):
            nums[i]=0

