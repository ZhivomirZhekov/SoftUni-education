# Input
name = input()
fail = 0
level = 1
average = 0
# logic
while True:
    grade = float(input())
    if grade < 4:
        fail += 1
        if fail > 1:
            print(f"{name} has been excluded at {level} grade")
            break
    elif grade >= 4 and level < 12:
        average += grade
        level += 1
    elif level == 12:
        average += grade
        print(f"{name} graduated. Average grade: {average/12:.2f}")
        break