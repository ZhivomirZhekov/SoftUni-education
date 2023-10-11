money_string = input().split(', ')
number_of_beggars = int(input())
money_integer = []
for money in money_string:
    money_integer.append(int(money))
beggars_money_sum = []
starting_index = 0
while starting_index < number_of_beggars:
    current_beggar = 0
    for beggar in range(starting_index, len(money_integer), number_of_beggars):
        current_beggar += money_integer[beggar]
    beggars_money_sum.append(current_beggar)
    starting_index += 1
print(beggars_money_sum)