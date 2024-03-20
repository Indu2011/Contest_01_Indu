class MyQueue:
    def __init__(self):
        self.st1 = []
        self.st2 = []
    def push(self, x: int) -> None:
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())
    def pop(self) -> int:
        return self.st1.pop()
        
    def peek(self) -> int:
        return self.st1[-1]

    def empty(self) -> bool:
        return not self.st1