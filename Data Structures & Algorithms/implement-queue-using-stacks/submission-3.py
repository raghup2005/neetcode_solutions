class MyQueue:

    def __init__(self):
        self.q=[]
        self.p=[]

        

    def push(self, x: int) -> None:
        self.q.append(x)

        

    def pop(self) -> int:
        if not self.p:
            while self.q:
                self.p.append(self.q.pop())
        return self.p.pop()

        

    def peek(self) -> int:
        if not self.p:
            while self.q:
                self.p.append(self.q.pop())
        return self.p[-1]
        

    def empty(self) -> bool:
        return max(len(self.q),len(self.p))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()