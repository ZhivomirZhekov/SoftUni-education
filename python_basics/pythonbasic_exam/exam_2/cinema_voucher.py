# Input
price_voucher = int(input())
# Logic
movie_tickets = 0
others = 0
while True:
    purchase = input()
    if purchase == 'End':
        break
    if len(purchase) > 8:

        price_voucher -= ord(purchase[0]) + ord(purchase[1])
        if price_voucher < 0:
            break
        movie_tickets += 1
    elif len(purchase) <= 8:

        price_voucher -= ord(purchase[0])
        if price_voucher < 0:
            break
        others += 1

print(f"{movie_tickets}")
print(f"{others}")