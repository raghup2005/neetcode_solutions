class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops=operations
        stk=[]
        for i in ops:
            if i=="+":
                stk.append(stk[-1]+stk[-2])
                
            elif i=="C":
                stk.pop()

            elif i=="D":
                stk.append(stk[-1]*2)
            else:
                stk.append(int(i))
        return sum(stk)