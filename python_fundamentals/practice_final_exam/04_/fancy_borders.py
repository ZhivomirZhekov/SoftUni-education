import re

number_of_potential_barcodes = int(input())
pattern = r'@#{1,}[A-Z][A-Za-z0-9]{4,}[A-Z]@#{1,}'
valid_barcodes = []
for number in range(number_of_potential_barcodes):
    potential_barcode = input()
    match = re.fullmatch(pattern , potential_barcode)
    if match:
        barcode = match.group()
        group = re.findall(r'\d+' , barcode)
        if group:
            print(f"Product group: {''.join(group)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")


