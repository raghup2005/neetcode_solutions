class Solution:
    def isValid(self, s: str) -> bool:
        stk=[]

        seen={")":"(","]":"[","}":"{"}
        for i in s:
            if i in seen:
                if stk and stk[-1]==seen[i]:
                    stk.pop()
                
                else:
                    return False


            else:
                stk.append(i)

        return len(stk)==0
        