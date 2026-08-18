class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        result=float("inf")

        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                result=min(r-left+1,result)
                total-=nums[left]
                left+=1
        if result==float("inf"):
            return 0
        return result