def rate(self_rarity: dict , self_rating: dict , plant: str , rating: int):
    if plant not in self_rarity.keys():
        print("error")
        return self_rating
    if plant not in self_rating:
        self_rating[plant] = []
    self_rating[plant].append(rating)
    return self_rating


def update(self: dict , plant: str , rarity: int):
    if plant not in self:
        print("error")
        return self
    self[plant] = rarity
    return self


def reset(self: dict , plant: str):
    if plant not in self:
        print("error")
        return self
    del self[plant]
    return self


number = int(input())
plant_rarity_dict = {}
plant_rating_dict = {}
for i in range(number):
    plant , rarity = input().split("<->")
    rarity = int(rarity)
    plant_rarity_dict[plant] = rarity

while True:
    command = input().split(": ")
    if command[0] == "Exhibition":
        break
    if command[0] == "Rate":
        plant , rating = command[1].split(" - ")
        rating = int(rating)
        plant_rating_dict = rate(plant_rarity_dict , plant_rating_dict , plant , rating)
    elif command[0] == "Update":
        plant , new_rarity = command[1].split(" - ")
        new_rarity = int(new_rarity)
        plant_rarity_dict = update(plant_rarity_dict , plant , new_rarity)
    elif command[0] == "Reset":
        plant = command[1]
        plant_rating_dict = reset(plant_rating_dict , plant)

print("Plants for the exhibition:")
for plant , rarity in plant_rarity_dict.items():
    if plant in plant_rating_dict:
        average_rating = sum(plant_rating_dict[plant]) / len(plant_rating_dict[plant])
    else:
        average_rating = 0
    print(f"- {plant}; Rarity: {rarity}; Rating: {average_rating:.2f}")
