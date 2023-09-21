# Input

movie_budged = float(input())
number_statists = int(input())
price_of_cloths_statists = float(input())

# Logic
cost_statist = number_statists * price_of_cloths_statists
decor = movie_budged * 0.1

if number_statists > 150:
    cost_statist *=0.9 # 0.9= 10% discount if statists are more than 150;

total_sum = decor + cost_statist
difference = abs(movie_budged - total_sum)
if total_sum > movie_budged:
    print(f'Not enough money!')
    print(f'Wingard needs {difference:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {difference:.2f} leva left.')

