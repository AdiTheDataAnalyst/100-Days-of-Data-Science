# Day 02 - Python Lists

skills = ["Python", "SQL", "Power BI", "Machine Learning"]

print("Original Skills:", skills)

# Add new skill
skills.append("Statistics")

# Remove a skill
skills.remove("SQL")

# Access an element
print("First Skill:", skills[0])

# Loop through list
print("\nMy Skills:")

for skill in skills:
    print(skill)

print("Total Skills:", len(skills))



# Python Tuples

student = ("Aditya", 25, "Data Science")

print("Student Name:", student[0])
print("Age:", student[1])
print("Course:", student[2])

print("Total Elements:", len(student))


# Python Dictionary

student = {
    "name": "Aditya",
    "age": 35,
    "course": "Data Science",
    "skills": ["Python", "SQL", "Power BI"]
}

print("Student Name:", student["name"])
print("Course:", student["course"])

# Add new information
student["experience"] = "Fresher"

# Update information
student["age"] = 36

# Display all information
for key, value in student.items():
    print(key, ":", value)



# Employee Salary Analysis

employees = {
    "Rahul": 35000,
    "Amit": 45000,
    "Priya": 55000,
    "Sneha": 40000,
    "Rohan": 60000
}

salaries = list(employees.values())

total_salary = sum(salaries)
average_salary = total_salary / len(salaries)
highest_salary = max(salaries)
lowest_salary = min(salaries)

print("Employee Salary Analysis")
print("-------------------------")

print("Total Employees:", len(employees))
print("Total Salary:", total_salary)
print("Average Salary:", average_salary)
print("Highest Salary:", highest_salary)
print("Lowest Salary:", lowest_salary)