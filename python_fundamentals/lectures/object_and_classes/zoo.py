class Zoo:
    __animals = 0

    def __init__(self , name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self , species , name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self , species: str):
        result = ""
        if species == "mammal":
            result += f"Mammals in {zoo_name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {zoo_name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            result += f"Birds in {zoo_name}: {', '.join(self.birds)}\n"
        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_name = input()
zoo = Zoo(zoo_name)
number = int(input())
for animal in range(number):
    species , name = input().split()
    zoo.add_animal(species, name)
get_info_species = input()
print(zoo.get_info(get_info_species))
