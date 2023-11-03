symbols = [char for char in input() if char != " "]
letters = {}
for char in symbols:
    if char not in letters.keys():
        letters[char] = 0
    letters[char] += 1

for key, value in letters.items():
    print(f"{key} -> {value}")
    