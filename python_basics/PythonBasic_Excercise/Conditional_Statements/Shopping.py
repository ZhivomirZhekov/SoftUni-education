# Input
budged_of_peter = float(input())
video_cards_number = int(input())
number_chipset = int(input())
ram_number = int(input())

# Logic
video_cards_price = 250 * video_cards_number
chipset_price = video_cards_price * 0.35
ram_price = video_cards_price * 0.1

total_chipset = number_chipset * chipset_price
total_ram = ram_number * ram_price

total_sum = video_cards_price + total_ram + total_chipset


if video_cards_number > number_chipset:
    total_sum *= 0.85

difference = abs(total_sum - budged_of_peter)

if total_sum <= budged_of_peter:
    print(f'You have {difference:.2f} leva left!')

else:
    print(f'Not enough money! You need {difference:.2f} leva more!')
