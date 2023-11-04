student_grade_counts = int(input())
student_grades_dict = {}
for count in range(student_grade_counts):
    student = input()
    grade = float(input())
    if student not in student_grades_dict.keys():
        student_grades_dict[student] = []
    student_grades_dict[student].append(grade)

for student , grades in student_grades_dict.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
