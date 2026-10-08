class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        max_sum=0
        count=float("inf")
        left=0
        for i in range(len(nums)):
            max_sum+=nums[i]

            while max_sum>=target:
                max_sum-=nums[left]
                count=min(count,i-left+1)
                left+=1
                
        if count==float("inf"):
            return 0
                
        return count
