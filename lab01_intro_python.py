# Lab 1: Introduction to Python - Artificial Intelligence
# Author: Mussa Khan
# Department: BS-AI (4th Year)
# Subject: Artificial Intelligence
# Instructor: Farhan Zafar Kayani

# ============================
# Task 1
# Accept 5 integer values from user, store them in a list and display the sum
# ============================

numbers = []

for i in range(5):
    value = int(input("Enter an integer value: "))
    numbers.append(value)

print("\nTask 1 Output")
print("List of numbers:", numbers)
print("Sum of numbers:", sum(numbers))


# ============================
# Task 2
# Create a dictionary of students and grades
# Write a function to add new student data
# ============================

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


# ============================
# Task 3
# Function that accepts a list of integers and returns it sorted in ascending order
# ============================

def sort_list(int_list):
    return sorted(int_list)

example_list = [12, 4, 7, 1, 9]

print("\nTask 3 Output")
print("Original list:", example_list)
print("Sorted list:", sort_list(example_list))


# ============================
# Task 4
# Create a tuple of the first five elements of the periodic table
# Demonstrate how to access elements
# ============================

elements = ("Hydrogen", "Helium", "Lithium", "Beryllium", "Boron")

print("\nTask 4 Output")
print("Tuple:", elements)
print("First element:", elements[0])
print("Third element:", elements[2])
print("Last element:", elements[-1])


# ============================
# Task 5
# Function that accepts two numbers and returns their sum
# ============================

def add_numbers(a, b):
    return a + b

print("\nTask 5 Output")
print("Sum of 7 and 3 is:", add_numbers(7, 3))
