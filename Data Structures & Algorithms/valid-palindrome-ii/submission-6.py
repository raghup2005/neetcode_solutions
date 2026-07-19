class Solution:
        
    def validPalindrome(self, s: str):
        def ch_pal(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        i=0
        j=len(s)-1
        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
          
            else:
                return (ch_pal(i+1,j) or ch_pal(i,j-1))
               
        return True 
