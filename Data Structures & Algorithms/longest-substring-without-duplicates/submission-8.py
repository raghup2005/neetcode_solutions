class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        count=0


        char_set=set()
        
        for i in range(len(s)):
            while s[i] in char_set:
                char_set.remove(s[l])
                l+=1

            char_set.add(s[i])
            count=max(count,i-l+1)
        return count
            
        