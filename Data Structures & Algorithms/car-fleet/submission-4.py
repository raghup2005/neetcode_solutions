class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]):
        n=len(position)
        car=[]
        for i in range(n):
            car.append([position[i],speed[i]])
            car.sort(key=lambda x:x[0],reverse=True)
        stack=[]
        for i,n in car:
            time=(target-i)/n
            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)

        