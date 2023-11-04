number_of_commands = int(input())

parking_lot_dict = {}

# •	"register {username} {license_plate_number}":
# The system only supports one car per user at the moment,
# so if a user tries to register another license plate using the same username, the system should print:
# "ERROR: already registered with plate number {license_plate_number}"
#   If the check above passes successfully, the user should be registered, so the system should print:
#  "{username} registered {license_plate_number} successfully"
# •	"unregister {username}":
# 	If the user is not present in the database, the system should print:
# "ERROR: user {username} not found"
# If the check above passes successfully, the system should print:
# "{username} unregistered successfully"

for number in range(number_of_commands):
    command = input().split()
    if "register" == command[0]:
        user_name = command[1]
        license_plate = command[2]
        if user_name in parking_lot_dict:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            parking_lot_dict[user_name] = license_plate
            print(f"{user_name} registered {license_plate} successfully")
    if "unregister" == command[0]:
        user_name = command[1]
        if user_name not in parking_lot_dict:
            print(f"ERROR: user {user_name} not found")
        else:
            del parking_lot_dict[user_name]
            print(f"{user_name} unregistered successfully")


for username, license_plate_number in parking_lot_dict.items():
    print(f"{username} => {license_plate_number}")
