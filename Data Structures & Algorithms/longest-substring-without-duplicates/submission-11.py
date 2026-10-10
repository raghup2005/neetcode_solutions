class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup=set()
        seen=0
        left=0

        for i in range(len(s)):
            while s[i] in dup:
                dup.remove(s[left])
                left+=1
            
            dup.add(s[i])
            seen=max(seen,i-left+1)

        return seen
