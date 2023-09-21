# Input
months = int(input())
water_bill = 20
internet_bill = 15
total_bills = 0
other_bills = 0
total_electricity_bill = 0
total_other_bills = 0
# Logic
for i in range(months):
    electricity_bill = float(input())
    other_bills = 1.2 * (water_bill + internet_bill + electricity_bill)
    total_bills += water_bill + internet_bill + electricity_bill + other_bills
    total_other_bills += other_bills
    total_electricity_bill += electricity_bill
total_water_bill = months * water_bill
total_internet_bill = months * internet_bill
average_bill_monthly = total_bills / months
# Output
print(f"Electricity: {total_electricity_bill:.2f} lv")
print(f"Water: {total_water_bill:.2f} lv")
print(f"Internet: {total_internet_bill:.2f} lv")
print(f"Other: {total_other_bills:.2f} lv")
print(f"Average: {average_bill_monthly:.2f} lv")


