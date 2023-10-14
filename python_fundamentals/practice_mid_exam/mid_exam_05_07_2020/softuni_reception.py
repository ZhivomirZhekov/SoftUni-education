employee_1 = int(input())
employee_2 = int(input())
employee_3 = int(input())
students = int(input())
counter_of_hours = 0
sum_of_employees_students_per_hour = employee_1 + employee_2 + employee_3
while students > 0:
    counter_of_hours += 1
    if counter_of_hours % 4 == 0:
        continue
    students -= sum_of_employees_students_per_hour
print(f"Time needed: {counter_of_hours}h.")