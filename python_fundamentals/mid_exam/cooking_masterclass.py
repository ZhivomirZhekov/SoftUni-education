from math import ceil
budget = float(input())
students = int(input())
flour_price = float(input())
eggs_price = float(input())
ten_eggs_price = eggs_price * 10
price_apron = float(input())
free_flour = 0
if students >= 5:
    free_flour = (students // 5) * flour_price

total_flour = flour_price * students
total_eggs = ten_eggs_price * students
total_apron = price_apron * (ceil(students * 1.2))
total_cost = (total_flour - free_flour) + total_eggs + total_apron
difference = total_cost - budget
if budget >= total_cost:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{difference:.2f}$ more needed.")



