maiden_party_price = float(input())
qty_love_letters = int(input())
qty_roses = int(input())
keychain = int(input())
qty_caricature = int(input())
qty_lucky_surprise = int(input())

price_love_letters = qty_love_letters * 0.6
price_roses = qty_roses * 7.2
price_keychain = keychain * 3.6
price_caricature = qty_caricature * 18.2
price_lucky_surprise = qty_lucky_surprise * 22

total_qty = qty_love_letters + qty_roses + keychain + qty_caricature + qty_lucky_surprise

if total_qty >= 25:
    total_income = (price_love_letters + price_roses + price_keychain + price_caricature + price_lucky_surprise) * 0.65
else:
    total_income = price_love_letters + price_roses + price_keychain + price_caricature + price_lucky_surprise
total_income *= 0.9
maiden_party_price -= total_income

if maiden_party_price <= 0:
    print(f"Yes! {abs(maiden_party_price):.2f} lv left.")
else:
    print(f"Not enough money! {maiden_party_price:.2f} lv needed.")
