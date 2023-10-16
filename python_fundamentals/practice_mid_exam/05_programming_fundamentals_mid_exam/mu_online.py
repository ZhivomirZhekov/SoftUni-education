dungeons = input().split("|")
health = 100
bitcoins = 0
best_room = 0
for room in dungeons:
    room_list = room.split()
    command = room_list[0]
    amount = int(room_list[1])
    if command == 'potion':
        health += amount
        healed = amount
        if health > 100:
            healed = 100 - (health - amount)
            health = 100
        print(f"You healed for {healed} hp.")
        print(f"Current health: {health} hp.")
        best_room += 1
    elif command == 'chest':
        bitcoins += amount
        print(f"You found {amount} bitcoins.")
        best_room += 1
    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
            best_room += 1
        else:
            best_room += 1
            print(f"You died! Killed by {command}.")
            print(f"Best room: {best_room}")
            break
if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

