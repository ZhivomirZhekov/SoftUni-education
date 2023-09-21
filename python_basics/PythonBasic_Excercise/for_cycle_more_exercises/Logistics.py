# Input
cargo = int(input())
# Logic
total_cargo_mass = 0
total_cargo = 0
bus = 0
truck = 0
train = 0
price = 0
for i in range(cargo):
    cargo_mass = int(input())
    if cargo_mass <= 3:
        bus += cargo_mass
        price += cargo_mass * 200
    elif 3 < cargo_mass < 12:
        truck += cargo_mass
        price += cargo_mass * 175
    elif 12 <= cargo_mass:
        train += cargo_mass
        price += cargo_mass * 120
    total_cargo_mass += cargo_mass
rms_cargo_price = price / total_cargo_mass
percentage_bus = bus / total_cargo_mass * 100
percentage_truck = truck / total_cargo_mass * 100
percentage_train = train / total_cargo_mass * 100
# Output
print(f'{rms_cargo_price:.2f}')
print(f'{percentage_bus:.2f}%')
print(f'{percentage_truck:.2f}%')
print(f'{percentage_train:.2f}%')

