# Lab 1: Introduction to Python

## 📌 Lab Overview

This lab introduces fundamental Python programming concepts including lists, dictionaries, tuples, and functions. Students learn to work with basic data structures and perform common operations.

## 🎯 Learning Objectives

- Accept and process user input
- Work with Python lists and perform operations
- Create and manipulate dictionaries
- Implement custom functions
- Understand tuple immutability and indexing
- Practice basic algorithmic thinking

## 📝 Tasks

### Task 1: Sum of User-Entered Values

**Objective:** Accept 5 integers from the user, store them in a list, and display their sum.

**Implementation:**
```python
numbers = []

for i in range(5):
    value = int(input("Enter an integer value: "))
    numbers.append(value)

print("\nTask 1 Output")
print("List of numbers:", numbers)
print("Sum of numbers:", sum(numbers))
```

**Key Concepts:**
- List initialization and `append()` method
- Loop iteration with `range()`
- Built-in `sum()` function
- User input handling with `input()`

---

### Task 2: Student Grades Dictionary

**Objective:** Create a dictionary to store student names and grades, then implement a function to add new students.

**Implementation:**
```python
students = {
    "Ali": "A",
    "Sara": "B",
    "Hassan": "A+"
}

def add_student(name, grade):
    students[name] = grade

# Adding example values
add_student("Zara", "A")

print("\nTask 2 Output")
print("Student Dictionary:", students)
```

**Key Concepts:**
- Dictionary creation and initialization
- Key-value pair manipulation
- Function definition with parameters
- Dictionary update operations

---

### Task 3: List Sorting Function

**Objective:** Create a function that accepts a list of integers and returns it sorted in ascending order.

**Implementation:**
```python
def sort_list(int_list):
    return sorted(int_list)

example_list = [12, 4, 7, 1, 9]

print("\nTask 3 Output")
print("Original list:", example_list)
print("Sorted list:", sort_list(example_list))
```

**Key Concepts:**
- Function definition and return values
- Built-in `sorted()` function
- List immutability with `sorted()` vs `sort()`

**Output Example:**
```
Original list: [12, 4, 7, 1, 9]
Sorted list: [1, 4, 7, 9, 12]
```

---

### Task 4: Periodic Table Tuple

**Objective:** Create a tuple containing the first five elements of the periodic table and demonstrate element access.

**Implementation:**
```python
elements = ("Hydrogen", "Helium", "Lithium", "Beryllium", "Boron")

print("\nTask 4 Output")
print("Tuple:", elements)
print("First element:", elements[0])
print("Third element:", elements[2])
print("Last element:", elements[-1])
```

**Key Concepts:**
- Tuple creation with immutability
- Positive indexing (0-based)
- Negative indexing (from the end)
- Tuple vs List differences

**Output Example:**
```
Tuple: ('Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron')
First element: Hydrogen
Third element: Lithium
Last element: Boron
```

---

### Task 5: Addition Function

**Objective:** Create a function that accepts two numbers and returns their sum.

**Implementation:**
```python
def add_numbers(a, b):
    return a + b

print("\nTask 5 Output")
print("Sum of 7 and 3 is:", add_numbers(7, 3))
```

**Key Concepts:**
- Function parameters
- Return statements
- Basic arithmetic operations

---

## 💡 Key Takeaways

1. **Lists** are mutable, ordered collections perfect for storing sequences
2. **Dictionaries** provide fast key-based lookup for structured data
3. **Tuples** are immutable and useful for fixed collections
4. **Functions** encapsulate reusable logic with clear inputs and outputs
5. Python provides powerful built-in functions like `sum()` and `sorted()`

## 🔗 Related Files

- **Source Code:** [lab01_intro_python.py](../lab01_intro_python.py)
- **Next Lab:** [Lab 2: Python Data Structures](lab02_python_basics.md)

---

*Author: Mussa Khan | BS-AI (4th Year)*
