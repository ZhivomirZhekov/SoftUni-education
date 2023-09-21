# Input
inheritance = float(input())
year_to_live = int(input())
years = year_to_live - 1800
# Logic
for i in range(years+1):
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= 12000 + (50*(18+i))
# Output
if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.')
else:
    print(f'He will need {abs(inheritance):.2f} dollars to survive.')