# Lab 3: NumPy and Pandas - Data Analysis Fundamentals
# Author: Mussa Khan
# Department: BS-AI (4th Year)
# Subject: Artificial Intelligence
# Instructor: Farhan Zafar Kayani

# ================================================
# LAB TASKS: NumPy and Pandas
# ================================================

# ------------------------------------------------
# Task 1: NumPy Array Operations
# ------------------------------------------------

import numpy as np

print("\n--- Task 1: NumPy Array Operations ---")

# Create NumPy array from a list
arr = np.array([1, 2, 3, 4, 5])
print("NumPy Array:", arr)

# Reshape array (5 rows, 1 column)
reshaped = arr.reshape(5, 1)
print("Reshaped Array:\n", reshaped)

# Slicing example
print("First three elements:", arr[:3])

# Mathematical operations
print("Array multiplied by 2:", arr * 2)

# Generate a random 3x3 array
random_arr = np.random.rand(3, 3)
print("\nRandom Array:\n", random_arr)

# Statistical operations
print("Mean:", np.mean(random_arr))
print("Median:", np.median(random_arr))
print("Standard Deviation:", np.std(random_arr))


# ------------------------------------------------
# Task 2: Pandas DataFrame Manipulation
# ------------------------------------------------

import pandas as pd

print("\n--- Task 2: Pandas DataFrame Manipulation ---")

# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Example: reading from CSV (commented because no file provided)
# df = pd.read_csv("data.csv")

# Handle missing values (fill NaN with 0)
df.fillna(0, inplace=True)

# Filtering: show rows where Age is greater than 28
filtered_df = df[df["Age"] > 28]
print("\nFiltered Data (Age > 28):\n", filtered_df)

# Sorting by Salary
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary (Descending):\n", sorted_df)


# ------------------------------------------------
# Task 3: Data Analysis Using Pandas
# ------------------------------------------------

print("\n--- Task 3: Data Analysis Using Pandas ---")

# Grouping and aggregation
grouped_data = df.groupby("Age").sum()
print("Grouped Data (Sum by Age):\n", grouped_data)

# Apply function to modify column
df["Salary"] = df["Salary"].apply(lambda x: x * 1.1)
print("\nUpdated Salaries (10 percent increase):\n", df)

# Create another DataFrame to merge
df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", "David"],
    "Department": ["HR", "IT", "Finance"]
})

# Merge DataFrames on "Name"
merged_df = pd.merge(df, df2, on="Name", how="left")
print("\nMerged DataFrame:\n", merged_df)


# ------------------------------------------------------
# Conclusion:
# ------------------------------------------------------
# In this lab I learned how to use NumPy and Pandas for data handling.
# I practiced creating arrays, reshaping, slicing and computing statistics.
# I also worked with DataFrames including indexing, filtering, sorting,
# grouping and merging. These tasks improved my understanding of how Python
# is used in real data analysis workflows.
