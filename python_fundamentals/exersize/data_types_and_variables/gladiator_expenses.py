lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_helmet_broke = lost_fights // 2
total_sword_broke = lost_fights // 3
total_shield_broke = lost_fights // (2*3)
total_armor_broke = total_shield_broke // 2
total_helmet_price = helmet_price * total_helmet_broke
total_sword_price = sword_price * total_sword_broke
total_shield_price = shield_price * total_shield_broke
total_armor_price = armor_price * total_armor_broke
total_price = total_helmet_price + total_sword_price + total_shield_price + total_armor_price
print(f"Gladiator expenses: {total_price:.2f} aureus")
