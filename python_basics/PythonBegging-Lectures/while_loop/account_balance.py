total = 0
while True:
    money = input()
    if money == 'NoMoreMoney':
        print(f'Total: {total:.2f}')
        break
    elif 0 < float(money):
        print(f'Increase: {float(money):.2f}')
        total += float(money)

    elif float(money) < 0:
        print('Invalid operation!')
        print(f'Total: {total:.2f}')
        break
