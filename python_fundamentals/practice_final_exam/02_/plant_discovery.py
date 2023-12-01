def rate(plant_rarity: dict , plant_rating: dict , plant: str , rating: int):
    if plant in plant_rarity.keys():
        if plant not in plant_rating.keys():
            plant_rating[plant] = []
        plant_rating[plant].append(rating)
    else:
        print("error")
    return plant_rating


def update(plant_rarity: dict , plant: str , new_rarity: int):
    if plant in plant_rarity.keys():
        plant_rarity[plant] = new_rarity
    else:
        print("error")
    return plant_rarity


def reset(plant_rating , plant):
    if plant in plant_rating.keys():
        del plant_rating[plant]
    else:
        print("error")
    return plant_rating


def main_function():
    number_of_plants = int(input())
    plant_rarity = {}
    plant_rating = {}
    for number in range(number_of_plants):
        plant , rarity = input().split("<->")
        plant_rarity[plant] = int(rarity)

    while True:
        command = input().split(": ")
        action = command[0]
        if action == "Exhibition":
            break

        if action == "Rate":
            plant , rating = command[1].split(" - ")
            rating = int(rating)
            plant_rating = rate(plant_rarity , plant_rating , plant , rating)
        elif action == "Update":
            plant , new_rarity = command[1].split(" - ")
            new_rarity = int(new_rarity)
            plant_rarity = update(plant_rarity , plant , new_rarity)
        elif action == "Reset":
            plant = command[1]
            plant_rating = reset(plant_rating , plant)
    print("Plants for the exhibition:")
    for plant , rarity in plant_rarity.items():
        if plant in plant_rating.keys():
            average_rating = sum(plant_rating[plant]) / len(plant_rating[plant])
        else:
            average_rating = 0
        print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")


main_function()
