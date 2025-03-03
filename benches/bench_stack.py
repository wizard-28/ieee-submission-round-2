import timeit
import matplotlib.pyplot as plt
import random
from ieee_submission.stack import Stack

# Define test stack sizes
stack_sizes = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]


# Warm-up function
def warmup(stack):
    for _ in range(10000):
        stack.push(random.randint(1, 100000))
        stack.pop()


# Function to run multiple trials and average the results
def run_trials(func, stack_size, trials=5):
    times = []
    for _ in range(trials):
        times.append(func(stack_size))
    return sum(times) / trials


# Function to benchmark push operation
def benchmark_push(stack_size):
    stack = Stack()
    warmup(stack)
    return timeit.timeit(
        lambda: stack.push(random.randint(1, 100000)), number=stack_size
    )


# Function to benchmark pop operation
def benchmark_pop(stack_size):
    stack = Stack()
    for _ in range(stack_size):
        stack.push(random.randint(1, 100000))
    warmup(stack)
    return timeit.timeit(lambda: stack.pop(), number=stack_size)


# Function to benchmark top operation
def benchmark_top(stack_size):
    stack = Stack()
    for _ in range(stack_size):
        stack.push(random.randint(1, 100000))
    warmup(stack)
    return timeit.timeit(lambda: stack.top(), number=stack_size)


# Function to benchmark getMin operation
def benchmark_getMin(stack_size):
    stack = Stack()
    for _ in range(stack_size):
        stack.push(random.randint(1, 100000))
    warmup(stack)
    return timeit.timeit(lambda: stack.getMin(), number=stack_size)


# Function to benchmark getMax operation
def benchmark_getMax(stack_size):
    stack = Stack()
    for _ in range(stack_size):
        stack.push(random.randint(1, 100000))
    warmup(stack)
    return timeit.timeit(lambda: stack.getMax(), number=stack_size)


# Collect benchmark data using multiple trials
push_times = [run_trials(benchmark_push, n) for n in stack_sizes]
pop_times = [run_trials(benchmark_pop, n) for n in stack_sizes]
top_times = [run_trials(benchmark_top, n) for n in stack_sizes]
min_times = [run_trials(benchmark_getMin, n) for n in stack_sizes]
max_times = [run_trials(benchmark_getMax, n) for n in stack_sizes]

# Normalize times to per-operation time
push_times = [t / n for t, n in zip(push_times, stack_sizes)]
pop_times = [t / n for t, n in zip(pop_times, stack_sizes)]
top_times = [t / n for t, n in zip(top_times, stack_sizes)]
min_times = [t / n for t, n in zip(min_times, stack_sizes)]
max_times = [t / n for t, n in zip(max_times, stack_sizes)]

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(stack_sizes, push_times, label="Push", marker="o")
plt.plot(stack_sizes, pop_times, label="Pop", marker="s")
plt.plot(stack_sizes, top_times, label="Top", marker="^")
plt.plot(stack_sizes, min_times, label="GetMin", marker="x")
plt.plot(stack_sizes, max_times, label="GetMax", marker="d")

plt.xlabel("Stack Size")
plt.ylabel("Time per Operation (seconds)")
plt.title("Benchmarking Stack Operations")
plt.legend()
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.savefig("assets/bench_stack.png")
