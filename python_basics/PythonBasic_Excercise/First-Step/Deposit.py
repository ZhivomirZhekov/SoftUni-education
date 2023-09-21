deposit = float(input())
time_range_deposit = int(input())/100
year_interest = float(input())
sum = deposit + time_range_deposit * ((deposit * year_interest) / 12)
print(sum)
