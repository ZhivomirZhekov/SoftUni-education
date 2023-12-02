def car_create(car_name , mileage , fuel):
    return {"car_name": car_name , "mileage": mileage , "fuel": fuel}


def drive(cars , car_name , distance , fuel):
    for car in cars:
        if car["car_name"] == car_name:
            if car["fuel"] >= fuel:
                car["fuel"] -= fuel
                car["mileage"] += distance
                print(f'{car["car_name"]} driven for {distance} kilometers. {fuel} liters of fuel consumed.')
                if car["mileage"] >= 100000:
                    print(f'Time to sell the {car["car_name"]}!')
                    cars.remove(car)
                return cars
            else:
                print("Not enough fuel to make that ride")
                return cars



def refuel(cars , max_fuel , car_name , fuel):
    for car in cars:
        if car['car_name'] == car_name:
            before_refuel = car['fuel']
            car['fuel'] = min(max_fuel , before_refuel + fuel)
            refueled = car['fuel'] - before_refuel
            print(f"{car['car_name']} refueled with {refueled} liters")
            return cars


def revert(cars , car_name , kilometers):
    for car in cars:
        if car['car_name'] == car_name:
            car['mileage'] -= kilometers
            if car['mileage'] < 10000:
                car['mileage'] = 10000
                return cars
            else:
                print(f"{car['car_name']} mileage decreased by {kilometers} kilometers")
                return cars


def main_function():
    number_of_cars = int(input())
    cars = []
    for _ in range(number_of_cars):
        car_name , mileage , fuel = input().split("|")
        mileage = int(mileage)
        fuel = int(fuel)
        cars.append(car_create(car_name , mileage , fuel))
    while True:
        command = input().split(" : ")
        action = command[0]
        if action == "Stop":
            break

        if action == "Drive":
            car_name = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            cars = drive(cars , car_name , distance , fuel)
        elif action == "Refuel":
            max_fuel = 75
            car_name = command[1]
            fuel = int(command[2])
            cars = refuel(cars , max_fuel , car_name , fuel)
        elif action == "Revert":
            car_name = command[1]
            kilometers = int(command[2])
            cars = revert(cars , car_name , kilometers)
    for car in cars:
        print(f"{car['car_name']} -> Mileage: {car['mileage']} kms, Fuel in the tank: {car['fuel']} lt.")


main_function()
