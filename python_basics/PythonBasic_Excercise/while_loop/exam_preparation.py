# Input
bad_grades = int(input())
average_grade = 0
count_bad_grades = 0
count_exercises = 0
last_exercise_solved = ''
#  Logic
current_exercise = input()
is_failed = False
while current_exercise != 'Enough':
    current_score = int(input())
    if current_score <= 4:
        count_bad_grades += 1
        if count_bad_grades == bad_grades:
            is_failed = True
            break
    average_grade += current_score
    count_exercises += 1
    last_exercise_solved = current_exercise
    current_exercise = input()
# Output
if is_failed:
    print(f"You need a break, {count_bad_grades} poor grades.")
else:
    average_grade /= count_exercises
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {count_exercises}")
    print(f"Last problem: {last_exercise_solved}")