# Input
budged = float(input())
season = input()
spend_money = 0
destination = ''
place = ''
# Logic
if budged <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        place = 'Camp'
        spend_money = budged * 0.3
    elif season == "winter":
        place = 'Hotel'
        spend_money = budged * 0.7
elif budged <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        place = 'Camp'
        spend_money = budged * 0.4
    elif season == "winter":
        place = 'Hotel'
        spend_money = budged * 0.8
elif budged > 1000:
    destination = 'Europe'
    place = 'Hotel'
    spend_money = budged * 0.9

# Output
print(f'Somewhere in {destination}')
print(f'{place} - {spend_money:.2f}')