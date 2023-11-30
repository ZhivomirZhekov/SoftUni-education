def add_stop(travel_stops , index , string):
    if 0 < index < len(travel_stops):
        travel_stops = travel_stops[:index] + string + travel_stops[index:]
    return travel_stops


def remove_stop(travel_stops , start_index , end_index):
    if 0 < start_index < len(travel_stops) and 0 < end_index < len(travel_stops):
        string_to_remove = travel_stops[start_index:end_index + 1]
        travel_stops = travel_stops.replace(string_to_remove , "")
    return travel_stops


def switch(travel_stops , old_string , new_string):
    if old_string in travel_stops:
        travel_stops = travel_stops.replace(old_string , new_string)
    return travel_stops


def main_function():
    travel_stops = input()
    while True:
        command = input()
        if command == 'Travel':
            break
        command = command.split(":")
        action = command[0]
        if action == "Add Stop":
            index = int(command[1])
            string = command[2]
            travel_stops = add_stop(travel_stops , index , string)
            print(travel_stops)
        elif action == "Remove Stop":
            start_index = int(command[1])
            end_index = int(command[2])
            travel_stops = remove_stop(travel_stops , start_index , end_index)
            print(travel_stops)
        elif action == "Switch":
            old_string = command[1]
            new_string = command[2]
            travel_stops = switch(travel_stops , old_string , new_string)
            print(travel_stops)
    print(f"Ready for world tour! Planned stops: {travel_stops}")


main_function()
