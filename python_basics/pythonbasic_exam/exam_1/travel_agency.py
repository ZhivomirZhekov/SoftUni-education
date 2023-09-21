# Input
name_city = input()
type_holiday_pack = input()
vip_status = input()
days_staying = int(input())
total = 0
# Logic
if days_staying > 7:
    days_staying -= 1
if days_staying > 0:
    if name_city == 'Bansko' or name_city == 'Borovets':
        if vip_status == "yes":
            if type_holiday_pack == "noEquipment":
                total = 80 * 0.95 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            elif type_holiday_pack == "withEquipment":
                total = 100 * 0.9 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            else:
                print("Invalid input!")
        elif vip_status == 'no':
            if type_holiday_pack == "noEquipment":
                total = 80 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            elif type_holiday_pack == "withEquipment":
                total = 100 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            else:
                print("Invalid input!")
    elif name_city == 'Varna' or name_city == 'Burgas':
        if vip_status == "yes":
            if type_holiday_pack == "noBreakfast":
                total = 100 * 0.93 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            elif type_holiday_pack == "withBreakfast":
                total = 130 * 0.88 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            else:
                print("Invalid input!")
        elif vip_status == 'no':
            if type_holiday_pack == "noBreakfast":
                total = 100 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            elif type_holiday_pack == "withBreakfast":
                total = 130 * days_staying
                print(f"The price is {total:.2f}lv! Have a nice time!")
            else:
                print("Invalid input!")
    else:
        print("Invalid input!")
else:
    print("Days must be positive number!")



