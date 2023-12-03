liked_guests_meals = {}
dislike_counter = 0

while True:
    command = input().split("-")
    action = command[0]
    if action == "Stop":
        break

    if action == "Like":
        guest = command[1]
        meal = command[2]
        if guest not in liked_guests_meals.keys():
            liked_guests_meals[guest] = []
        if meal not in liked_guests_meals[guest]:
            liked_guests_meals[guest].append(meal)

    elif action == "Dislike":
        guest = command[1]
        meal = command[2]
        if guest not in liked_guests_meals.keys():
            print(f"{guest} is not at the party.")
            continue
        if meal not in liked_guests_meals[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            liked_guests_meals[guest].remove(meal)
            dislike_counter += 1
            print(f"{guest} doesn't like the {meal}.")

for guest , meals in liked_guests_meals.items():
    print(f"{guest}: {', '.join(meals)}")
print(f"Unliked meals: {dislike_counter}")