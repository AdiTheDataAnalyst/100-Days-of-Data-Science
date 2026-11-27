# Day 03 - Python Functions

def greet():
    print("Welcome to day 3!")
    print("Learning Python Functions.")

greet()    


# Function with Parameters

def students_info(name, age, course):
    print("Student Name:", name)
    print("Age:", age)
    print("Course:", course)

students_info("Aditya", 25, "Data Science") 
students_info("Chandu", 22, "Machine Learning")
students_info("Abhijeet", 28, "Artificial Intelligence")   


# Functions with Return Statement

def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

result = calculate_average(80, 90, 85)

print("Average Marks:", result)


# Lambda Functions

# Normal function

def square(x):
    return x * x

print(square(5))


# Lambda function

square_lambda = lambda x: x * x

print(square_lambda(5))


# Map Function

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))

print(squares)

# Map Function with real world example

salaries = [30000, 40000, 50000, 60000]

updated_salaries = list(
    map(lambda x: x * 1.10, salaries)
)

print(updated_salaries)


# Filter Function

numbers = [10, 15, 20, 25, 30, 35, 40]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)

# Filter Function with real world example
salaries = [25000, 35000, 45000, 55000, 65000]

high_salary = list(
    filter(lambda x: x > 40000, salaries)
)

print(high_salary)


# Reduce Function
from functools import reduce

numbers = [10, 20, 30, 40, 50]

total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)




# Mini Data Analytics Project

from functools import reduce

employees = {
    "Rahul": 30000,
    "Amit": 45000,
    "Priya": 55000,
    "Sneha": 40000,
    "Rohan": 65000
}

# Extract salaries
salaries = list(employees.values())

# Calculate total salary
total = reduce(lambda a, b: a + b, salaries)

# Calculate average salary
average = total / len(salaries)

# Increase salaries by 10%
updated = list(map(lambda x: x * 1.10, salaries))

# Find employees earning above 40000
high_salary = dict(
    filter(lambda item: item[1] > 40000, employees.items())
)

print("Employee Salary Analysis")
print("------------------------")

print("Total Salary:", total)
print("Average Salary:", average)
print("Updated Salaries:", updated)
print("High Salary Employees:", high_salary)