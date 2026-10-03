class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count=0
        count=0
        seen={}

        for i in range(len(nums)):
            seen[nums[i]]=seen.get(nums[i],0)+1

        for i in seen:
            if seen[i]>max_count:
                max_count=seen[i]
                count=i

        return count


            
        