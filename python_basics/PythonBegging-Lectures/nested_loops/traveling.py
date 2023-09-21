total_saved = 0
while True:
    destination = input()
    if destination == 'End':
        break
    minimum_budget = float(input())
    total_saved = 0
    while True:
        savings = float(input())
        total_saved += savings
        if total_saved >= minimum_budget:
            print(f"Going to {destination}!")
            break
