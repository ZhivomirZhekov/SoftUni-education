animals = input()
#   list_of_animals = animals.replace(', ' , ' ')
list_of_animals = animals.split(', ')
if list_of_animals.index('wolf') == len(list_of_animals) - 1:
    print("Please go away and stop eating my sheep")
else:
    if list_of_animals.index('wolf') == 0:
        number_sheep = len(list_of_animals) - 1
        print(f"Oi! Sheep number {number_sheep}! You are about to be eaten by a wolf!")
    else:
        number_sheep = len(list_of_animals) - (list_of_animals.index('wolf') + 1)
        print(f"Oi! Sheep number {number_sheep}! You are about to be eaten by a wolf!")
# string = input()
# herd = string.split(", ")
# if herd[-1] == "wolf":
#     print("Please go away and stop eating my sheep")
# else:
#     herd_count = len(herd)
#     wolf_index = herd.index("wolf")
#     sheep_in_danger_index = (len(herd) - 1) - wolf_index
#     print(f"Oi! Sheep number {sheep_in_danger_index}! You are about to be eaten by a wolf!")