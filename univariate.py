# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:32:20 2023

@author: Divya Shree
"""

# Import necessary libraries
import pandas as pd

# Load the dataset from the CSV file
file_path = "C:\\Users\\Divya Shree\\Downloads\\creditcard (1).csv"
df = pd.read_csv(file_path)

# a. Fetch basic information
basic_info = df.info()

# b. Get the count of quantitative, qualitative, nominal, categorical data
# Quantitative data (numerical)
quantitative_data = df.select_dtypes(include=['int64', 'float64'])
quantitative_count = len(quantitative_data.columns)

# Qualitative data (non-numerical)
qualitative_data = df.select_dtypes(exclude=['int64', 'float64'])
qualitative_count = len(qualitative_data.columns)

# Nominal data (categorical but with no specific order)
nominal_data = qualitative_data.select_dtypes(include=['object'])
nominal_count = len(nominal_data.columns)

# c. Display descriptive statistics
descriptive_stats = df.describe()

# d. Check for duplicate values
duplicates = df[df.duplicated()]

# e. Know the unique values in a particular column
unique_values_column = df['Amount'].unique()

# f. Check for null or missing values
null_values = df.isnull().sum()

# Replace missing values (if needed)
# You can replace missing values with methods like fillna or by using a specific strategy like mean, median, mode, etc.
# Example: df['column_name'].fillna(value, inplace=True)

# g. Know data types of all attributes
data_types = df.dtypes

# Print or display the results
print("a. Basic Information:")
print(basic_info)

print("\nb. Count of Data Types:")
print(f"Quantitative (Numerical) Data: {quantitative_count} columns")
print(f"Qualitative (Non-Numerical) Data: {qualitative_count} columns")
print(f"Nominal Data (Categorical): {nominal_count} columns")

print("\nc. Descriptive Statistics:")
print(descriptive_stats)

print("\nd. Duplicate Values:")
print(duplicates)

print("\ne. Unique Values in a Particular Column:")
print(unique_values_column)

print("\nf. Null or Missing Values:")
print(null_values)

print("\ng. Data Types of All Attributes:")
print(data_types)
