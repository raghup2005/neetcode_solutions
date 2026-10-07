class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        j=0

        window=set()
        max_count=0

        for i in range(len(s)):
            while s[i] in window:
                window.remove(s[j])
                j+=1

            window.add(s[i])
            max_count=max(max_count,i-j+1)

        return max_count            
            

            
        