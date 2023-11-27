import re

string = input()
pattern = r"(?i)([#|])([a-z\s]+)(\1)(\d{2}\/\d{2}\/\d{2})(\1)(\d+)(\1)"
matches = re.findall(pattern , string)
total_calories = sum(int(match[5]) for match in matches)
days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for element in matches:
    item_name = element[1]
    expiration_date = element[3]
    calories = element[5]
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
# import re
#
# text_input = input()
# pattern = r"(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
# matches = re.findall(pattern , text_input)
# total_days = 0
# for match in matches:
#     calories = int(match[3])
#     total_days += calories
# total_days = total_days // 2000
# print(f"You have food to last you for: {total_days} days!")
# for match in matches:
#     item_name , expiration_date , calories = match[1] , match[2] , int(match[3])
#     print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")
