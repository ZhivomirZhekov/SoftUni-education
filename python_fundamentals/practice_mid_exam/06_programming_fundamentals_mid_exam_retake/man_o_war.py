def fire(warship: list, index: int, damage: int):
    if 0 <= index < len(warship):
        warship[index] -= damage
        if warship[index] <= 0 :
            print("You won! The enemy ship has sunken.")
            exit()
    return warship


def defend(pirate_ship: list, start_index: int, end_index: int, damage: int):
    if 0 <= start_index and end_index < len(pirate_ship):
        for section in range(start_index, end_index + 1):
            pirate_ship[section] -= damage
            if pirate_ship[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return pirate_ship


def repair(pirate_ship: list, index: int, health: int, max_health_section: int):
    if 0 <= index < len(pirate_ship):
        pirate_ship[index] += health
        if pirate_ship[index] > max_health_section:
            pirate_ship[index] = max_health_section
    return pirate_ship

def status(pirate_ship: list, max_health_section: int):
    counter = 0
    low_health = max_health_section * 0.2
    for section in pirate_ship:
        if section < low_health:
            counter += 1
    print(f"{counter} sections need repair.")


pirate_ship = input().split(">")
warship = input().split(">")
pirate_ship = [int(x) for x in pirate_ship]
warship = [int(x) for x in warship]
max_health_section = int(input())

while True:
    command = input().split()
    if command[0] == "Retire":
        break
    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        fire(warship, index, damage)
    if command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        defend(pirate_ship, start_index, end_index, damage)
    if command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        repair(pirate_ship, index, health, max_health_section)
    if command[0] == "Status":
        status(pirate_ship, max_health_section)

if 0 not in warship and 0 not in pirate_ship:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(warship)}")