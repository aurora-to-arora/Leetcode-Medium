from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        # rotate the queue until the last pushed is at front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
        return self.q.popleft()  # this is the top of the stack

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0
