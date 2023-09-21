budget = float(input())
salary = 0

while True:
    if budget < 0:
        print(f"We need {abs(budget):.2f} leva for our actors.")
        break
    actor = input()
    if actor == 'ACTION':
        print(f"We are left with {budget:.2f} leva.")
        break

    if len(actor) < 16:
        salary = float(input())
        budget -= salary
    else:
        salary = budget * 0.2
        budget -= salary