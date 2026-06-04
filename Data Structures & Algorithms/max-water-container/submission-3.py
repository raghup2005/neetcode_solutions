class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        max_water=0
        while i<j:
            width=j-i
            height=min(heights[i],heights[j])
            area=width*height
            max_water=max(area,max_water)

            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return max_water

        