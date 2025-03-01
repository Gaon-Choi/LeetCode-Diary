class MyStack:

    def __init__(self):
        self.size: int = 0
        self.queue: List[int] = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.size += 1
        

    def pop(self) -> int:
        elem: int = self.queue.pop(self.size - 1)
        self.size -= 1
        
        return elem

    def top(self) -> int:
        if self.size == 0:
            return None

        return self.queue[self.size - 1]
        

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()