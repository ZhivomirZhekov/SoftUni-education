required_money = float(input())
money_in_hand = float(input())
total_days_counter = 0
total_spend_money = 0
spending_in_a_row = False

while money_in_hand < required_money:
    action = input()
    current_sum = float(input())
    total_days_counter += 1

    if action == 'spend':
        total_spend_money += 1
        if total_spend_money == 5:
            spending_in_a_row = True
            break
        money_in_hand -= current_sum
        if money_in_hand < 0:
            money_in_hand = 0

    elif action == 'save':
        money_in_hand += current_sum
        total_spend_money = 0  # Reset spending streak

if spending_in_a_row:
    print("You can't save the money.")
    print(total_days_counter)
else:
    print(f"You saved the money for {total_days_counter} days.")