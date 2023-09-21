weight_package = float(input())
type_service = input()
distance = int(input())
total = 0
if type_service == 'standard':
    if 1 > weight_package :
        total = distance * 3
    elif 1 <= weight_package < 10:
        total = distance * 5
    elif 10 <= weight_package < 40:
        total = distance * 10
    elif 40 <= weight_package < 90:
        total = distance * 15
    elif 90 <= weight_package <= 150:
        total = distance * 20
if type_service == 'express':
    if 1 > weight_package:
        express = 3 * 0.8 * weight_package
        total = distance * 3 + express * distance
    elif 1 <= weight_package < 10:
        express = 5 * 0.4 * weight_package
        total = distance * 5 + express * distance
    elif 10 <= weight_package < 40:
        express = 10 * 0.05 * weight_package
        total = distance * 10 + express * distance
    elif 40 <= weight_package < 90:
        express = 15 * 0.02 * weight_package
        total = distance * 15 + express * distance
    elif 90 <= weight_package <= 150:
        express = 20 * 0.01 * weight_package
        total = distance * 20 + express * distance
total /= 100
print(f"The delivery of your shipment with weight of {weight_package:.3f} kg. would cost {total:.2f} lv.")
