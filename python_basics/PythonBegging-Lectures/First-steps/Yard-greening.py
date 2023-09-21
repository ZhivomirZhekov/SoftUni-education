price_square = 7.61
square_meters_to_green = float(input())
total_sum = price_square * square_meters_to_green
discount_price = total_sum * 0.18
final_price = total_sum-discount_price
print(f'The final price is: {final_price} lv.')
print(f'The discount is: {discount_price} lv.')
