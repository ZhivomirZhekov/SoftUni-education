mackerel_price = float(input())
sprat_price = float(input())
bonito_kilo = float(input())
scad_kilo = float(input())
mussel_kilo = int(input())
bonito_price = 1.6 * mackerel_price * bonito_kilo
scad_price = 1.8 * sprat_price * scad_kilo
mussel_price = 7.5 * mussel_kilo
total_price = bonito_price + scad_price + mussel_price
print("%.2f" % total_price)

