countries = input().split(", ")
capitals = input().split(", ")
countries_capitals = {countries[index]: capitals[index] for index in range(len(countries))}

for country, capital in countries_capitals.items():
    print(f"{country} -> {capital}")

