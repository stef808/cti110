# CTI-110
# P2HW2 - List
# morales stefan
# 06/08/2023

# Initialize an empty list for storing grades
grades = []

# Loop over each module number from 1 to 6
for i in range(1, 7):
    # Prompt the user to enter the grade for the current module
    grade = float(input(f"Enter grade for Module {i}: "))
    
    # Append the grade to the grades list
    grades.append(grade)

# Calculate the minimum grade, maximum grade, sum, and average of grades
min_grade = min(grades)
max_grade = max(grades)
sum_grades = sum(grades)
avg_grades = sum_grades / len(grades)

# Display the calculated values
print("\n--------Results--------")
print(f"Lowest Grade: {min_grade}")
print(f"Highest Grade: {max_grade}")
print(f"Sum of Grades: {sum_grades}")
print(f"Average: {avg_grades:.2f}")
print("--------------------------------")