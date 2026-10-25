class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        left=0
        right=len(nums)-1

        while left<right:
            nums[left],nums[right]=nums[right],nums[left]

            left+=1
            right-=1

        l=0
        r=k-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        
        le=k
        ri=len(nums)-1

        while le<ri:
            nums[le],nums[ri]=nums[ri],nums[le]
            le+=1
            ri-=1

        return nums