course_dict = {}

while True:
    command = input()
    if command == "end":
        break
    course_name , student_name = command.split(' : ')
    if course_name not in course_dict:
        course_dict[course_name] = []
    course_dict[course_name].append(student_name)

for course_name, registered_students in course_dict.items():
    print(f"{course_name}: {len(registered_students)}")
    for student_name in registered_students:
        print(f"-- {student_name}")