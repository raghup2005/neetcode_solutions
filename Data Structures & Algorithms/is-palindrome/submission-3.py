class Solution:
    def isPalindrome(self, s: str) -> bool:
        char=""
        for i in s:
            if i.isalnum():
                char+=i.lower()
        if char==char[::-1]:
            return True
        return False

    
        