seats_hall = int(input())
counter = 0
income = 0
while True:
    people = input()
    if people == 'Movie time!':
        print(f"There are {seats_hall} seats left in the cinema.")
        break
    if seats_hall < int(people):
        print("The cinema is full.")
        break
    if int(people) % 3 == 0:
        income += int(people) * 5 - 5
        seats_hall -= int(people)
    else:
        income += int(people) * 5
        seats_hall -= int(people)
print(f'Cinema income - {income} lv.')