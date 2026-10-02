class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        max_count=0
        max_num=0
        for i in range(len(nums)):
            seen[nums[i]]=seen.get(nums[i],0)+1
        for i in seen:
            if seen[i]>max_count:
                max_count=seen[i]
                max_num=i

        return max_num