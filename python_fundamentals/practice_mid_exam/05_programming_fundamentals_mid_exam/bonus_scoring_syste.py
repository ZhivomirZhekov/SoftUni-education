number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
student_max_points = 0
student_attendance_with_max_points = 0
for student in range(number_of_students):
    student_attendance = int(input())
    total_bonus = student_attendance / number_of_lectures * (5+additional_bonus)
    if student_max_points < total_bonus:
        student_max_points = total_bonus
        student_attendance_with_max_points = student_attendance

print(f"Max Bonus: {round(student_max_points)}.")
print(f"The student has attended {student_attendance_with_max_points} lectures.")
