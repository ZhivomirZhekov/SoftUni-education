# Input
change = float(input())
change = int(change * 100) # Converted to cents
# Logic
coin_counter = 0
coin_counter += change // 200
change = change % 200

coin_counter += change // 100
change = change % 100

coin_counter += change // 50
change = change % 50

coin_counter += change // 20
change = change % 20

coin_counter += change // 10
change = change % 10

coin_counter += change // 5
change = change % 5

coin_counter += change // 2
change = change % 2

coin_counter += change // 1
change = change % 1

print(coin_counter)