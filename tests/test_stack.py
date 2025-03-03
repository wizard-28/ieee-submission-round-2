import pytest
from ieee_submission.stack import Stack, EmptyStackError


def test_empty_stack_operations():
    """Test operations on an empty stack"""
    stack = Stack()

    # Test empty stack exceptions
    with pytest.raises(EmptyStackError):
        stack.pop()

    with pytest.raises(EmptyStackError):
        stack.top()

    with pytest.raises(EmptyStackError):
        stack.getMin()

    with pytest.raises(EmptyStackError):
        stack.getMax()


def test_single_element():
    """Test stack with a single element"""
    stack = Stack()
    stack.push(42)
    assert stack.top() == 42
    assert stack.getMin() == 42
    assert stack.getMax() == 42
    assert stack.pop() == 42

    # Should be empty after pop
    with pytest.raises(EmptyStackError):
        stack.getMin()


def test_ascending_order():
    """Test pushing elements in ascending order"""
    stack = Stack()
    elements = [1, 2, 3, 4, 5]
    for elem in elements:
        stack.push(elem)

    assert stack.getMin() == 1
    assert stack.getMax() == 5

    for i in range(len(elements) - 1, -1, -1):
        assert stack.getMin() == elements[0]
        assert stack.getMax() == elements[i]
        assert stack.pop() == elements[i]


def test_descending_order():
    """Test pushing elements in descending order"""
    stack = Stack()
    elements = [5, 4, 3, 2, 1]
    for elem in elements:
        stack.push(elem)

    for i in range(len(elements) - 1, -1, -1):
        assert stack.getMin() == elements[i]
        assert stack.getMax() == elements[0]
        assert stack.pop() == elements[i]


def test_random_order():
    """Test pushing elements in random order"""
    stack = Stack()
    elements = [3, 1, 5, 2, 4]
    for elem in elements:
        stack.push(elem)

    assert stack.getMin() == 1
    assert stack.getMax() == 5

    for i in range(len(elements) - 1, -1, -1):
        assert stack.getMin() == min(elements[: i + 1])
        assert stack.getMax() == max(elements[: i + 1])
        assert stack.pop() == elements[i]


def test_duplicate_elements():
    """Test stack with duplicate elements"""
    stack = Stack()
    elements = [3, 1, 3, 1, 3]
    for elem in elements:
        stack.push(elem)

    assert stack.getMin() == 1
    assert stack.getMax() == 3

    for i in range(len(elements) - 1, -1, -1):
        assert stack.top() == elements[i]
        assert stack.getMin() == min(elements[: i + 1])
        assert stack.getMax() == max(elements[: i + 1])
        assert stack.pop() == elements[i]


def test_alternating_push_pop():
    """Test alternating push and pop operations"""
    stack = Stack()
    # Push-pop sequence
    operations = [
        ("push", 5),
        ("push", 3),
        ("pop", 3),
        ("push", 7),
        ("push", 2),
        ("pop", 2),
        ("pop", 7),
        ("push", 1),
        ("push", 8),
        ("pop", 8),
        ("pop", 1),
        ("pop", 5),
    ]

    for op, val in operations:
        if op == "push":
            stack.push(val)
        else:  # op == "pop"
            assert stack.pop() == val


def test_min_max_after_operations():
    """Verify min/max is correct after various operations"""
    stack = Stack()
    # Push elements
    stack.push(5)
    stack.push(2)
    stack.push(7)
    stack.push(2)
    stack.push(9)

    # Verify initial state
    assert stack.getMin() == 2
    assert stack.getMax() == 9

    # Pop the max
    assert stack.pop() == 9
    assert stack.getMin() == 2
    assert stack.getMax() == 7

    # Pop one of the mins
    assert stack.pop() == 2
    assert stack.getMin() == 2
    assert stack.getMax() == 7

    # Pop the max again
    assert stack.pop() == 7
    assert stack.getMin() == 2
    assert stack.getMax() == 5

    # Pop the last min
    assert stack.pop() == 2
    assert stack.getMin() == 5
    assert stack.getMax() == 5

    # Pop the final element
    assert stack.pop() == 5

    # Should be empty now
    with pytest.raises(EmptyStackError):
        stack.getMin()
    with pytest.raises(EmptyStackError):
        stack.getMax()


def test_same_min_max_multiple_counts():
    """Test handling of multiple occurrences of the same min/max value"""
    stack = Stack()
    # Push multiple instances of the same min/max
    stack.push(3)  # min and max
    stack.push(3)  # min and max
    stack.push(3)  # min and max

    # Verify initial state
    assert stack.getMin() == 3
    assert stack.getMax() == 3

    # Pop one element
    assert stack.pop() == 3
    assert stack.getMin() == 3
    assert stack.getMax() == 3

    # Pop another element
    assert stack.pop() == 3
    assert stack.getMin() == 3
    assert stack.getMax() == 3

    # Pop final element
    assert stack.pop() == 3

    # Should be empty now
    with pytest.raises(EmptyStackError):
        stack.getMin()
    with pytest.raises(EmptyStackError):
        stack.getMax()


def test_only_stack_operations_edge_case():
    """Test situation where values are only unique in stack, never min or max"""
    stack = Stack()
    # First establish min and max
    stack.push(1)  # min
    stack.push(10)  # max

    # Now push intermediate values that don't change min/max
    stack.push(5)
    stack.push(7)
    stack.push(3)
    stack.push(4)

    assert stack.getMin() == 1
    assert stack.getMax() == 10

    # Pop intermediate values
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 7
    assert stack.pop() == 5

    # Min/max should still be the same
    assert stack.getMin() == 1
    assert stack.getMax() == 10

    # Pop the max and min
    assert stack.pop() == 10
    assert stack.getMin() == 1
    assert stack.getMax() == 1

    assert stack.pop() == 1

    # Should be empty now
    with pytest.raises(EmptyStackError):
        stack.getMin()
    with pytest.raises(EmptyStackError):
        stack.getMax()


def test_repeated_operations():
    """Test a sequence of repeated operations"""
    stack = Stack()

    # First sequence
    stack.push(5)
    stack.push(3)
    stack.push(7)
    assert stack.getMin() == 3
    assert stack.getMax() == 7
    stack.pop()  # Remove 7
    stack.pop()  # Remove 3
    assert stack.getMin() == 5
    assert stack.getMax() == 5

    # Second sequence
    stack.push(2)
    stack.push(8)
    assert stack.getMin() == 2
    assert stack.getMax() == 8
    stack.pop()  # Remove 8
    assert stack.getMin() == 2
    assert stack.getMax() == 5

    # Third sequence
    stack.push(1)
    stack.push(1)
    assert stack.getMin() == 1
    assert stack.getMax() == 5
    stack.pop()  # Remove 1
    assert stack.getMin() == 1
    assert stack.getMax() == 5
    stack.pop()  # Remove 1
    assert stack.getMin() == 2
    assert stack.getMax() == 5

    # Clean up
    stack.pop()  # Remove 2
    stack.pop()  # Remove 5
    with pytest.raises(EmptyStackError):
        stack.getMin()
