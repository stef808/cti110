# CTI-110
# P3HW1 - List
# Morales stefan
# 06/12/2023

# Initialize an empty list for storing grades
grades = []

# Loop over each module number from 1 to 6
for i in range(1, 7):
    # Prompt the user to enter the grade for the current module
    grade = float(input(f"Please enter your grade for Module {i}: "))
    
    # Append the grade to the grades list
    grades.append(grade)

# Calculate the minimum grade, maximum grade, sum, and average of grades
min_grade = min(grades)
max_grade = max(grades)
sum_grades = sum(grades)
avg_grades = sum_grades / len(grades)

# Determine the letter grade
if avg_grades >= 90:
    letter_grade = 'A'
elif avg_grades >= 80:
    letter_grade = 'B'
elif avg_grades >= 70:
    letter_grade = 'C'
elif avg_grades >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the calculated values
print("\n--------Results--------")
print(f"Lowest Grade: {min_grade}")
print(f"Highest Grade: {max_grade}")
print(f"Sum of Grades: {sum_grades}")
print(f"Average: {avg_grades:.2f}")
print("--------------------------------")
print(f"Your grade is: {letter_grade}")
