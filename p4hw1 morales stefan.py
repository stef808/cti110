# CTI-110

# P4HW1 - Score List

# morales stefan

# 06/15/2023


def get_grade(avg_score):
    if avg_score >= 90:
        return 'A'
    elif avg_score >= 80:
        return 'B'
    elif avg_score >= 70:
        return 'C'
    elif avg_score >= 60:
        return 'D'
    else:
        return 'F'

num_scores = int(input("How many scores do you want to enter? "))
scores_list = []

for i in range(num_scores):
    while True:
        score = float(input(f"Enter score #{i+1}: "))
        if 0 <= score <= 100:
            scores_list.append(score)
            break
        else:
            print("\nInvalid Score entered!!!!\nScore should be between 0 and 100")
            continue

lowest_score = min(scores_list)
scores_list.remove(lowest_score)

avg_score = sum(scores_list) / len(scores_list)
grade = get_grade(avg_score)

print("\n----------------Results---------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {scores_list}")
print(f"Scores Average : {avg_score:.2f}")
print(f"Grade          : {grade}")
print("--------------------------------------")
