points = 0
compare = 0
player = ''
name = ''
while True:
    if compare >= points:
        points = compare
        player = name
    name = input()
    compare = 0
    if name == 'Stop':
        break
    for i in range(len(name)):
        number = int(input())
        if number == ord(name[i]):
            compare += 10
        else:
            compare += 2
print(f"The winner is {player} with {points} points!")
