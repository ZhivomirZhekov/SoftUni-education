lessons_schedule = input().split(', ')
command = input()
while command != 'course start':
    command = command.split(':')
    if command[1] not in lessons_schedule:
        if command[0] == 'Add':
            lessons_schedule.append(command[1])
        elif command[0] == 'Insert':
            lessons_schedule.insert(int(command[2]) , command[1])
        elif command[0] == 'Exercise':
            lessons_schedule.append(command[1])
            lessons_schedule.append(f'{command[1]}-Exercise')
    elif command[1] in lessons_schedule:
        if command[0] == 'Remove':
            title_index = lessons_schedule.index(command[1])
            if title_index + 1 in range(len(lessons_schedule)):
                if "Exercise" in lessons_schedule[title_index + 1]:
                    lessons_schedule.pop(title_index + 1)
            lessons_schedule.remove(command[1])
        elif command[0] == 'Swap' and (command[1] and command[2] in lessons_schedule):
            if command[1] in lessons_schedule and command[2] in lessons_schedule:
                first_position = lessons_schedule.index(command[1])
                second_position = lessons_schedule.index(command[2])
                first_has_exercise = False
                second_has_exercise = False
                if first_position + 1 in range(len(lessons_schedule)):
                    first_has_exercise = "Exercise" in lessons_schedule[first_position + 1]
                if second_position + 1 in range(len(lessons_schedule)):
                    second_has_exercise = "Exercise" in lessons_schedule[second_position + 1]
                lessons_schedule[first_position] , lessons_schedule[second_position] = \
                    lessons_schedule[second_position] , lessons_schedule[first_position]
                if first_has_exercise and second_has_exercise:
                    lessons_schedule[first_position + 1] , lessons_schedule[second_position + 1] = \
                        lessons_schedule[second_position + 1] , lessons_schedule[first_position + 1]
                elif not first_has_exercise and second_has_exercise:
                    lessons_schedule.insert(first_position + 1 , lessons_schedule.pop(second_position + 1))
                elif first_has_exercise and not second_has_exercise:
                    lessons_schedule.insert(second_position + 1 , lessons_schedule.pop(first_position + 1))
        elif command[0] == 'Exercise':
            index_lesson = lessons_schedule.index(command[1])
            if f'{command[1]}-Exercise' not in lessons_schedule:
                lessons_schedule.insert(index_lesson+1, f'{command[1]}-Exercise')

    command = input()
for index in range(len(lessons_schedule)):
    print(f"{index+1}.{lessons_schedule[index]}")
