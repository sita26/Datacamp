import pandas as pd

# Step 1: Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Salary': [70000, 80000, 120000, 90000, 75000]
}

df = pd.DataFrame(data)

# Step 2: Display the DataFrame
print("DataFrame:")
print(df)

# Step 3: Basic Data Analysis
print("\nBasic Information:")
print(df.info())  # Overview of the dataset

print("\nSummary Statistics:")
print(df.describe())  # Statistical summary

# Step 4: Filtering data
high_salary = df[df['Salary'] > 80000]  # Filter rows with Salary > 80,000
print("\nEmployees with salary greater than 80,000:")
print(high_salary)

# Step 5: Adding a new column
df['Bonus'] = df['Salary'] * 0.1  # Add 10% of the salary as a bonus
print("\nDataFrame after adding Bonus column:")
print(df)

# Step 6: Grouping and Aggregation
avg_salary_by_city = df.groupby('City')['Salary'].mean()
print("\nAverage Salary by City:")
print(avg_salary_by_city)

# Step 7: Saving to a CSV file
df.to_csv('employee_data.csv', index=False)
print("\nData saved to 'employee_data.csv'")

