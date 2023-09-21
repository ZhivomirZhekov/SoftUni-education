pack_pens = 5.8
pack_markers = 7.2
detergent = 1.2
numb_pack_pens = int(input())
numb_pack_markers = int(input())
quantity_detergent = int(input())
discount = int(input())/100
dollar_pens = pack_pens*numb_pack_pens
dollar_markers = pack_markers*numb_pack_markers
dollar_detergent = detergent*quantity_detergent
sum_dollar = dollar_detergent+dollar_pens+dollar_markers
total = sum_dollar-(sum_dollar*discount)
print(total)

