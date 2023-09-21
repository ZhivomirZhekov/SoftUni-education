need_sum = int(input())
counter = 1
cash_paid = 0
card_paid = 0
total = 0
counter_cash = 0
counter_card = 0
while True:
    if total >= need_sum:
        print(f"Average CS: {cash_paid/counter_cash:.2f}")
        print(f"Average CC: {card_paid/counter_card:.2f}")
        break
    money = input()
    if money == 'End':
        print("Failed to collect required money for charity.")
        break

    else:
        if counter % 2 == 0:
            if int(money) > 10:
                card_paid += int(money)
                counter += 1
                total += int(money)
                counter_card += 1
                print("Product sold!")
            else:
                print("Error in transaction!")
                counter += 1
        else:
            if int(money) < 101:
                cash_paid += int(money)
                counter += 1
                total += int(money)
                counter_cash += 1
                print("Product sold!")
            else:
                print("Error in transaction!")
                counter += 1
