class MyQueue:

    def __init__(self):
        self.front = []
        self.back = []

    def push(self, x: int) -> None:
        self.front.append(x)
        

    def pop(self) -> int:
        while len(self.front) > 1:
            self.back.append(self.front.pop())

        temp = self.front.pop()

        while self.back:
            self.front.append(self.back.pop())

        return temp
        

    def peek(self) -> int:
        return self.front[0]
        

    def empty(self) -> bool:
        return len(self.front) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()