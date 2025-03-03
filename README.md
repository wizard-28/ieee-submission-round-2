# IEEE Round 2 Submission – Custom Data Structure Implementation

<!--toc:start-->

- [Level 1](#level-1)
  - [📌 Project Overview](#📌-project-overview)
  - [**🚀 Technologies Used**](#🚀-technologies-used)
  - [**🌟 Features Implemented**](#🌟-features-implemented)
  - [**🛠️ Setup Instructions**](#🛠️-setup-instructions)
    - [**Prerequisites**](#prerequisites)
    - [**Installation Steps**](#installation-steps)
    - [Usage](#usage)
    - [**Running Tests**](#running-tests)
  - [**📊 Implementation Details**](#📊-implementation-details)
    - [**Data Structures Used**](#data-structures-used)
    - [**Operations Complexity**](#operations-complexity)
  - [**🛠️ Code Quality**](#🛠️-code-quality)
  <!--toc:end-->

# Level 1

## 📌 Project Overview

This project implements a **Stack** data structure that supports the following operations in **O(1) time complexity** and **O(n) space complexity**:

- `push(x)`: Pushes element `x` onto the stack.
- `pop()`: Removes the top element from the stack.
- `top()`: Returns the top element without removing it.
- `getMin()`: Returns the smallest element in the stack.
- `getMax()`: Returns the largest element in the stack.

## **🚀 Technologies Used**

- **Language**: Python (>=3.13)
- **Development Tools**: Poetry, Pre-commit, MyPy, Ruff, Pytest
- **Version Control**: Git

## **🌟 Features Implemented**

✔️ Custom Stack implementation supporting all operations in **O(1) time** and **O(n) space**

✔️ Efficient tracking of **minimum** and **maximum** values using auxiliary double-ended queue

✔️ Unit tests using **Pytest**

✔️ Pre-commit hooks for linting & formatting

## **🛠️ Setup Instructions**

### **Prerequisites**

- Python **>=3.13+**
- Poetry package manager

### **Installation Steps**

1. Install [Python](https://www.python.org/) and [Poetry](https://python-poetry.org/)
2. Run the following commands:

```bash
# Clone the repository
git clone https://github.com/your-username/ieee-submission.git
cd ieee-submission

# Install dependencies
poetry install

# Activate virtual environment
eval $(poetry env activate)
```

### Usage

```bash
poetry run python -m ieee_submission

```

### **Running Tests**

```bash
pytest
```

## **📊 Implementation Details**

### **Data Structures Used**

- **Main Stack (`stack`)**: Stores the actual elements using a list
- **Auxiliary Deck (`aux`)**: Stores the min and max elements on the extreme left and right side of the deque respectively

### **Operations Complexity**

| Operation  | Time Complexity | Space Complexity |
| ---------- | --------------- | ---------------- |
| `push(x)`  | **O(1)**        | **O(n)**         |
| `pop()`    | **O(1)**        | **O(1)**         |
| `top()`    | **O(1)**        | **O(1)**         |
| `getMin()` | **O(1)**        | **O(1)**         |
| `getMax()` | **O(1)**        | **O(1)**         |

## **🛠️ Code Quality**

- Uses **Pre-commit hooks** for linting (`ruff`), static type checking (`mypy`), and code formatting
