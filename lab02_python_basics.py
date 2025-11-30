# Lab 2: Python Basics - Lists, Dictionaries, Tuples & Functions
# Author: Mussa Khan
# Department: BS-AI (4th Year)
# Subject: Artificial Intelligence
# Instructor: Farhan Zafar Kayani

# ======================================================
# Task 1: Sum of User-Entered Values
# Accept 5 integers from user, store in a list and show sum
# ======================================================

print("Enter 5 numbers:")
values = []   # list to store numbers

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    values.append(num)

print("Sum:", sum(values))


# ======================================================
# Task 2: Student Grades Dictionary
# Create dictionary and function to add new students
# ======================================================

students = {}

def add_student(student_dict, name, grade):
    student_dict[name] = grade

# Example of adding data
add_student(students, "Ali", "A")
add_student(students, "Sara", "B")

print("\nStudent Grades Dictionary:")
print(students)


# ======================================================
# Task 3: Sorting a List
# Function that returns a sorted list in ascending order
# ======================================================

def sort_list(numbers):
    return sorted(numbers)

sample_list = [12, 5, 9, 1, 7]
print("\nOriginal list:", sample_list)
print("Sorted list:", sort_list(sample_list))


# ======================================================
# Task 4: Accessing Tuple Elements
# Create a tuple of first 5 periodic table elements
# ======================================================

elements = ("Hydrogen", "Helium", "Lithium", "Beryllium", "Boron")

print("\nPeriodic Table Elements Tuple:")
print("First element:", elements[0])
print("Second element:", elements[1])
print("Last element:", elements[-1])


# ======================================================
# Task 5: Sum of Two Numbers
# Function that accepts two numbers and returns their sum
# ======================================================

def add_numbers(a, b):
    return a + b

print("\nSum of 7 and 3 is:", add_numbers(7, 3))


# ------------------------------------------------------
# Conclusion:
# In this lab I learned how to use basic Python structures 
# like lists, dictionaries, tuples and functions. 
# I practiced taking input from users, storing data and 
# performing simple operations such as sorting and summing values. 
# This lab helped me understand how to organize code better 
# and gave me more confidence in writing small Python programs.
# ------------------------------------------------------
