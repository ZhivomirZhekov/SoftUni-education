def car_attributes() -> dict:
    number_of_cars = int(input())
    cars_dict = {}
    _car_mileage = "mileage"
    _car_fuel = "fuel"
    for number in range(number_of_cars):
        car_mileage_fuel = input().split('|')
        _car = car_mileage_fuel[0]
        _mileage = int(car_mileage_fuel[1])
        _fuel = int(car_mileage_fuel[2])
        if _car not in cars_dict:
            cars_dict[_car] = {}
        cars_dict[_car][_car_mileage] = _mileage
        cars_dict[_car][_car_fuel] = _fuel
    return cars_dict


def drive(cars_dict: dict , _car: str , _distance: int , _fuel: int):
    _car_mileage = "mileage"
    _car_fuel = "fuel"
    if _car not in cars_dict.keys():
        return cars_dict
    elif cars_dict[_car][_car_fuel] <= _fuel:
        print("Not enough fuel to make that ride")
        return cars_dict
    else:
        cars_dict[_car][_car_mileage] += _distance
        cars_dict[_car][_car_fuel] -= _fuel
        print(f"{_car} driven for {_distance} kilometers. {_fuel} liters of fuel consumed.")
        if cars_dict[_car][_car_mileage] >= 100000:
            del cars_dict[_car]
            print(f"Time to sell the {_car}!")
            return cars_dict

        return cars_dict


def refuel(cars_dict: dict , _car: str , _fuel: int):
    tank_max_capacity = 75
    _car_fuel = "fuel"
    litters_to_fill = min(75 - cars_dict[_car][_car_fuel] , fuel)
    cars_dict[_car][_car_fuel] = min(cars_dict[_car][_car_fuel] + _fuel , tank_max_capacity)

    print(f"{_car} refueled with {litters_to_fill} liters")
    return cars_dict


def revert(cars_dict: dict , _car : str , kilometers: int):
    _car_mileage = "mileage"
    cars_dict[_car][_car_mileage] -= kilometers
    if cars_dict[_car][_car_mileage] < 10000:
        cars_dict[_car][_car_mileage] = 10000
    else:
        print(f"{_car} mileage decreased by {kilometers} kilometers")
    return cars_dict


cars = car_attributes()

while True:
    command = input().split(" : ")
    if command[0] == "Stop":
        break
    if command[0] == "Drive":
        car = command[1]
        distance = int(command[2])
        fuel = int(command[3])
        cars = drive(cars , car , distance , fuel)
    elif command[0] == "Refuel":
        car = command[1]
        fuel = int(command[2])
        refuel(cars , car , fuel)
    elif command[0] == "Revert":
        car = command[1]
        distance = int(command[2])
        revert(cars , car , distance)

for car , attributes in cars.items():
    car_mileage = "mileage"
    car_fuel = "fuel"
    mileage = attributes[car_mileage]
    fuel = attributes[car_fuel]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
