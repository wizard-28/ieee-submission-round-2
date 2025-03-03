from collections import deque


class EmptyStackError(Exception):
    """Custom exception raised when performing an operation on an empty stack."""

    def __init__(self, message: str) -> None:
        """Initialize the exception with a given error message."""
        super().__init__(message)
        self.message = message

    def __str__(self) -> str:
        """Return the error message when the exception is printed."""
        return f"{self.message}"


class Stack:
    """
    A stack data structure with O(1) time complexity for push, pop, top, getMin, and getMax operations.

    This stack efficiently tracks both the minimum and maximum values using an auxiliary deque.

    """

    stack: list[int]  # Main stack to store elements
    aux: deque[
        tuple[int, int]
    ]  # auxiliary deque (double ended queue) to track the min/max values and their counts

    def __init__(self) -> None:
        """Initialize an empty stack and an auxiliary deque for min/max tracking."""

        self.stack = []
        self.aux = deque()

    def push(self, x: int) -> None:
        """
        Push an integer onto the stack and update min/max tracking.

        Args:
            x (int): The value to push onto the stack.
        """

        self.stack.append(x)

        # If the auxiliary deque is empty, initialize with the first element
        if not self.aux:
            self.aux.append((x, 1))  # First element with count 1
            return

        # For minimum tracking (left side)
        if x < self.aux[0][0]:
            self.aux.appendleft((x, 1))  # New min with count 1
        elif x == self.aux[0][0]:
            self.aux[0] = (x, self.aux[0][1] + 1)  # Increment count

        # For maximum tracking (right side)
        if x > self.aux[-1][0]:
            self.aux.append((x, 1))  # New max with count 1
        elif x == self.aux[-1][0]:
            self.aux[-1] = (x, self.aux[-1][1] + 1)  # Increment count

    def pop(self) -> int:
        """
        Remove and return the top element from the stack while updating min/max tracking.

        Returns:
            int: The popped element.

        Raises:
            EmptyStackError: If the stack is empty.
        """

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
        # We need to check `self.aux` too as it may be empty from the previous `popleft`
        if self.aux and val == self.aux[-1][0]:
            if self.aux[-1][1] > 1:
                self.aux[-1] = (val, self.aux[-1][1] - 1)  # Decrement count
            else:
                self.aux.pop()  # Remove if count reaches 0

        return val

    def top(self) -> int:
        """
        Return the top element of the stack without removing it.

        Returns:
            int: The top element of the stack.

        Raises:
            EmptyStackError: If the stack is empty.
        """

        if not self.stack:
            raise EmptyStackError("Top from an empty stack")
        return self.stack[-1]

    def getMin(self) -> int:
        """
        Return the minimum element in the stack.

        Returns:
            int: The minimum element.

        Raises:
            EmptyStackError: If the stack is empty.
        """

        if not self.aux:
            raise EmptyStackError("Stack is empty")
        return self.aux[0][0]

    def getMax(self) -> int:
        """
        Return the maximum element in the stack.

        Returns:
            int: The maximum element.

        Raises:
            EmptyStackError: If the stack is empty.
        """

        if not self.aux:
            raise EmptyStackError("Stack is empty")
        return self.aux[-1][0]
