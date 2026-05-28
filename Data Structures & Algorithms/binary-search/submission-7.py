class Solution:
    def search(self,nums,target):
        left=0
        right=len(nums)
        while left<right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                left+=1
            elif target<nums[mid]:
                right-=1
        return -1





        