counter_coffees = 0
while True:
    command = input()
    if command == 'END':
        break
    if command.lower() == 'coding' or command.lower() == 'dog' \
            or command.lower() == 'cat' or command.lower() == 'movie':
        if command.islower() :
            counter_coffees += 1
        else:  # if command.isupper()
            counter_coffees += 2
if counter_coffees > 5:
    print('You need extra sleep')
else:
    print(counter_coffees)