class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current_val=0

        min_sub=float("inf")
        left=0

        for i in range(len(nums)):
            current_val+=nums[i]

            while current_val>=target:
                current_val-=nums[left]
                min_sub=min(min_sub,i-left+1)
                left+=1
        if min_sub==float("inf"):
            return 0

        return min_sub
        