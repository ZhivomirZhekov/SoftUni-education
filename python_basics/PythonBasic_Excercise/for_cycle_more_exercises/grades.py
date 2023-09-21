# Input
total_students = int(input())
# Logic
poor_students = 0
middle_students = 0
good_students = 0
top_students = 0
sum_grades = 0
for i in range(total_students):
    grade = float(input())
    if 2 <= grade < 3:
        poor_students += 1
    elif 3 <= grade < 4:
        middle_students += 1
    elif 4 <= grade < 5:
        good_students += 1
    elif grade >= 5:
        top_students += 1
    sum_grades += grade
percent_top = top_students / total_students * 100
percent_good = good_students / total_students * 100
percent_middle = middle_students / total_students * 100
percent_poor = poor_students / total_students * 100
average_grade = sum_grades / total_students
# Output
print(f'Top students: {percent_top:.2f}%')
print(f'Between 4.00 and 4.99: {percent_good:.2f}%')
print(f'Between 3.00 and 3.99: {percent_middle:.2f}%')
print(f'Fail: {percent_poor:.2f}%')
print(f'Average: {average_grade:.2f}')