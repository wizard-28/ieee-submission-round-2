from collections import deque


class EmptyStackError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        return f"{self.message}"


class Stack:
    stack: list[int]
    aux: deque[tuple[int, int]]

    def __init__(self) -> None:
        self.stack = []
        self.aux = deque()

    def push(self, x: int) -> None:
        self.stack.append(x)

        # For minimum tracking (left side)
        if not self.aux or x < self.aux[0][0]:
            self.aux.appendleft((x, 1))  # New min with count 1
        elif x == self.aux[0][0]:
            self.aux[0] = (x, self.aux[0][1] + 1)  # Increment count

        # For maximum tracking (right side)
        if not self.aux or x > self.aux[-1][0]:
            self.aux.append((x, 1))  # New max with count 1
        elif x == self.aux[-1][0]:
            self.aux[-1] = (x, self.aux[-1][1] + 1)  # Increment count

    def pop(self) -> int:
        if not self.stack:
            raise EmptyStackError("Pop from an empty stack")

        val = self.stack.pop()

        # Update min tracking
        if val == self.aux[0][0]:
            if self.aux[0][1] > 1:
                self.aux[0] = (val, self.aux[0][1] - 1)  # Decrement count
            else:
                self.aux.popleft()  # Remove if count reaches 0

        # Update max tracking
        if val == self.aux[-1][0]:
            if self.aux[-1][1] > 1:
                self.aux[-1] = (val, self.aux[-1][1] - 1)  # Decrement count
            else:
                self.aux.pop()  # Remove if count reaches 0

        return val

    def top(self) -> int:
        if not self.stack:
            raise EmptyStackError("Top from an empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.aux:
            raise EmptyStackError("Stack is empty")
        return self.aux[0][0]

    def getMax(self) -> int:
        if not self.aux:
            raise EmptyStackError("Stack is empty")
        return self.aux[-1][0]
