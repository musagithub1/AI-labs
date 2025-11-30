# Lab 3: NumPy and Pandas - Data Analysis Fundamentals

## 📌 Lab Overview

This lab introduces two essential Python libraries for data science: **NumPy** for numerical computing and **Pandas** for data manipulation. These tools form the foundation of modern data analysis and machine learning workflows.

## 🎯 Learning Objectives

- Understand NumPy array operations and transformations
- Perform statistical computations on numerical data
- Create and manipulate Pandas DataFrames
- Filter, sort, and aggregate data effectively
- Merge and combine datasets from multiple sources

## 📚 Libraries Used

```python
import numpy as np
import pandas as pd
```

---

## 📝 Tasks

### Task 1: NumPy Array Operations

**Objective:** Explore NumPy array creation, reshaping, slicing, and statistical operations.

#### Array Creation and Manipulation

```python
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
```

**Output:**
```
NumPy Array: [1 2 3 4 5]
Reshaped Array:
 [[1]
  [2]
  [3]
  [4]
  [5]]
First three elements: [1 2 3]
Array multiplied by 2: [ 2  4  6  8 10]
```

#### Random Array Generation and Statistics

```python
# Generate a random 3x3 array
random_arr = np.random.rand(3, 3)
print("\nRandom Array:\n", random_arr)

# Statistical operations
print("Mean:", np.mean(random_arr))
print("Median:", np.median(random_arr))
print("Standard Deviation:", np.std(random_arr))
```

**Key Concepts:**
- **Array Broadcasting:** Vectorized operations on entire arrays
- **Reshaping:** Changing array dimensions without copying data
- **Slicing:** Efficient subsetting with `[start:end]` syntax
- **Statistical Functions:** Built-in aggregations for data analysis

---

### Task 2: Pandas DataFrame Manipulation

**Objective:** Create DataFrames, handle missing values, filter data, and sort records.

#### DataFrame Creation

```python
# Create a DataFrame from a dictionary
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)
```

**Output:**
```
      Name  Age  Salary
0    Alice   25   50000
1      Bob   30   60000
2  Charlie   35   70000
```

#### Data Cleaning and Filtering

```python
# Handle missing values (fill NaN with 0)
df.fillna(0, inplace=True)

# Filtering: show rows where Age is greater than 28
filtered_df = df[df["Age"] > 28]
print("\nFiltered Data (Age > 28):\n", filtered_df)

# Sorting by Salary
sorted_df = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary (Descending):\n", sorted_df)
```

**Key Concepts:**
- **Boolean Indexing:** Filter rows using conditional expressions
- **Missing Data Handling:** `fillna()`, `dropna()` for data cleaning
- **Sorting:** `sort_values()` with custom ordering

---

### Task 3: Advanced Data Analysis

**Objective:** Perform grouping, aggregation, transformation, and merging operations.

#### Grouping and Aggregation

```python
# Grouping and aggregation
grouped_data = df.groupby("Age").sum()
print("Grouped Data (Sum by Age):\n", grouped_data)
```

#### Data Transformation

```python
# Apply function to modify column (10% salary increase)
df["Salary"] = df["Salary"].apply(lambda x: x * 1.1)
print("\nUpdated Salaries (10 percent increase):\n", df)
```

**Lambda Functions:** Anonymous functions for quick transformations.

#### Merging DataFrames

```python
# Create another DataFrame to merge
df2 = pd.DataFrame({
    "Name": ["Alice", "Bob", "David"],
    "Department": ["HR", "IT", "Finance"]
})

# Merge DataFrames on "Name"
merged_df = pd.merge(df, df2, on="Name", how="left")
print("\nMerged DataFrame:\n", merged_df)
```

**Output:**
```
      Name  Age  Salary Department
0    Alice   25   55000         HR
1      Bob   30   66000         IT
2  Charlie   35   77000        NaN
```

**Merge Types:**
- **Inner:** Only matching keys
- **Left:** All from left + matching from right
- **Right:** All from right + matching from left
- **Outer:** All records from both

---

## 💡 Key Takeaways

### NumPy Benefits
✅ **Performance:** 10-100x faster than Python lists  
✅ **Memory Efficient:** Optimized storage for numerical data  
✅ **Vectorization:** Operate on entire arrays without loops  
✅ **Broadcasting:** Automatic shape alignment for operations  

### Pandas Benefits
✅ **Tabular Data:** Natural representation for structured data  
✅ **Missing Data:** Built-in handling for NaN values  
✅ **Data Alignment:** Automatic label-based alignment  
✅ **Time Series:** Powerful tools for temporal data  

## 🎓 Skills Acquired

- NumPy array creation, reshaping, and slicing
- Statistical computations (mean, median, std)
- DataFrame construction from dictionaries
- Data filtering with boolean indexing
- Sorting and ordering datasets
- Applying transformations with `apply()` and lambda
- Merging multiple DataFrames

## 🔍 Real-World Applications

- **Data Preprocessing:** Cleaning datasets for ML models
- **Exploratory Data Analysis:** Understanding data distributions
- **Feature Engineering:** Creating new features from existing data
- **Data Integration:** Combining data from multiple sources

## 🔗 Related Files

- **Source Code:** [lab03_numpy_pandas.py](../lab03_numpy_pandas.py)
- **Previous Lab:** [Lab 2: Python Data Structures](lab02_python_basics.md)
- **Next Lab:** [Lab 4: Graph Traversal Algorithms](lab04_bfs_dfs.md)

---

*Author: Mussa Khan | BS-AI (4th Year)*
