class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        count=float("inf")
        left=0
        k=0

        for i in range(len(nums)):
            k+=nums[i]
            
            while k>=target:
                count=min(count,i-left+1)
                k-=nums[left]
                left+=1
            
        if count==float("inf"):
            return 0

        return count
