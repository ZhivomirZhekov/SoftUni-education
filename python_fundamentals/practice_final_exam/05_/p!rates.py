cities = {}
command = input().split("||")
while command[0] != "Sail":
    city , population , gold = command[0] , int(command[1]) , int(command[2])
    if city not in cities.keys():
        cities[city] = {'population': 0 , "gold": 0}
    cities[city]["population"] += population
    cities[city]["gold"] += gold
    command = input().split("||")
command = input().split("=>")
while command[0] != "End":
    action = command[0]
    if action == "Plunder":
        town, people , gold = command[1] , int(command[2]) , int(command[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        cities[town]["population"] -= people
        cities[town]["gold"] -= gold
        if cities[town]["population"] == 0 or cities[town]["gold"] == 0:
            cities.pop(town)
            print(f"{town} has been wiped off the map!")
    elif action == "Prosper":
        town , gold = command[1] , int(command[2])
        if gold < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            cities[town]['gold'] += gold
            total_gold = cities[town]['gold']
            print(f"{gold} gold added to the city treasury. {town} now has {total_gold} gold.")
    command = input().split("=>")
if cities:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, city_info in cities.items():
        people = city_info["population"]
        gold = city_info["gold"]
        print(f"{city} -> Population: {people} citizens, Gold: {gold} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")