class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen={}
        j=0
        res=0
        for i in range(len(s)):
            seen[s[i]]=seen.get(s[i],0)+1

            while (i-j+1)-max(seen.values())>k:
                seen[s[j]]-=1
                j+=1

            res=max(res,i-j+1)

        return res