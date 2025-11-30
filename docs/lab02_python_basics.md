# Lab 2: Python Data Structures

## 📌 Lab Overview

This lab builds upon fundamental Python concepts by diving deeper into data structure manipulation. Students practice working with lists, dictionaries, tuples, and functions to solve practical problems.

## 🎯 Learning Objectives

- Master list operations and iteration
- Implement dictionary-based data management
- Apply sorting algorithms
- Understand tuple properties and access patterns
- Design reusable functions with clear interfaces

## 📝 Tasks

### Task 1: Sum of User-Entered Values

**Objective:** Accept 5 integers from user input, store them in a list, and calculate their sum.

**Implementation:**
```python
print("Enter 5 numbers:")
values = []   # list to store numbers

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    values.append(num)

print("Sum:", sum(values))
```

**Key Concepts:**
- F-string formatting for dynamic prompts
- List accumulation with `append()`
- Aggregate operations with `sum()`

**Sample Interaction:**
```
Enter 5 numbers:
Enter number 1: 10
Enter number 2: 20
Enter number 3: 15
Enter number 4: 30
Enter number 5: 25
Sum: 100
```

---

### Task 2: Student Grades Management System

**Objective:** Create a dictionary to manage student grades and implement a function to add new entries.

**Implementation:**
```python
students = {}

def add_student(student_dict, name, grade):
    student_dict[name] = grade

# Example of adding data
add_student(students, "Ali", "A")
add_student(students, "Sara", "B")

print("\nStudent Grades Dictionary:")
print(students)
```

**Key Concepts:**
- Empty dictionary initialization
- Function parameters including mutable objects
- Dictionary as a data store
- In-place modification of dictionaries

**Advanced Note:** 
The function accepts the dictionary as a parameter, demonstrating how mutable objects can be modified within functions without returning them.

---

### Task 3: List Sorting Utility

**Objective:** Implement a function that returns a sorted copy of a list in ascending order.

**Implementation:**
```python
def sort_list(numbers):
    return sorted(numbers)

sample_list = [12, 5, 9, 1, 7]
print("\nOriginal list:", sample_list)
print("Sorted list:", sort_list(sample_list))
```

**Key Concepts:**
- Non-destructive sorting with `sorted()`
- Function return values
- Maintaining original data integrity

**Output:**
```
Original list: [12, 5, 9, 1, 7]
Sorted list: [1, 5, 7, 9, 12]
```

---

### Task 4: Periodic Table Elements

**Objective:** Create a tuple of the first 5 periodic table elements and demonstrate various indexing techniques.

**Implementation:**
```python
elements = ("Hydrogen", "Helium", "Lithium", "Beryllium", "Boron")

print("\nPeriodic Table Elements Tuple:")
print("First element:", elements[0])
print("Second element:", elements[1])
print("Last element:", elements[-1])
```

**Key Concepts:**
- Tuple immutability
- Zero-based indexing
- Negative indexing for reverse access
- Accessing elements at specific positions

**Why use tuples?**
Tuples are ideal for fixed collections that shouldn't change, like the periodic table elements.

---

### Task 5: Number Addition Function

**Objective:** Create a simple function that adds two numbers together.

**Implementation:**
```python
def add_numbers(a, b):
    return a + b

print("\nSum of 7 and 3 is:", add_numbers(7, 3))
```

**Key Concepts:**
- Function definition syntax
- Parameter passing
- Return value usage
- Function composition

---

## 💡 Advanced Concepts Learned

### Data Structure Selection
- **Lists:** When order matters and data changes
- **Dictionaries:** When you need fast lookups by key
- **Tuples:** When data should remain constant

### Function Design Principles
1. **Single Responsibility:** Each function does one thing well
2. **Clear Parameters:** Descriptive parameter names
3. **Predictable Returns:** Consistent return types
4. **No Side Effects:** Avoid unexpected modifications (when possible)

## 🎓 Skills Acquired

✅ User input validation and processing  
✅ Dynamic data collection with lists  
✅ Dictionary-based key-value storage  
✅ Sorting algorithms and built-in functions  
✅ Tuple indexing and immutability concepts  
✅ Function composition and reusability  

## 🔗 Related Files

- **Source Code:** [lab02_python_basics.py](../lab02_python_basics.py)
- **Previous Lab:** [Lab 1: Introduction to Python](lab01_intro_python.md)
- **Next Lab:** [Lab 3: NumPy and Pandas](lab03_numpy_pandas.md)

---

*Author: Mussa Khan | BS-AI (4th Semester)*
