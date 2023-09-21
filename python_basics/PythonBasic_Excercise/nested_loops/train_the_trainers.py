jury_number = int(input())
total_presentations = 0
average_grade = 0
final_grade = 0
command = input()
while command != 'Finish':
    current_presentation_name = command
    total_presentations += 1
    presentations_grade = 0
    for grade in range(jury_number):
        current_grade = float(input())
        presentations_grade += current_grade
    presentation_average_grade = presentations_grade / jury_number
    print(f"{current_presentation_name} - {presentation_average_grade:.2f}.")
    final_grade += presentation_average_grade
    command = input()
final_average_grade = final_grade / total_presentations
print(f"Student's final assessment is {final_average_grade:.2f}." )