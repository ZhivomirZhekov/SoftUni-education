resources = {}

while True:
    current_resources = input()
    if current_resources == 'stop':
        break
    amount_resources = int(input())
    if current_resources not in resources.keys():
        resources[current_resources] = 0
    resources[current_resources] += amount_resources

for key, values in resources.items():
    print(f"{key} -> {values}")

