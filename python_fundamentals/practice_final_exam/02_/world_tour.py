def add_stop(string: str , index_to_add: int , string_to_add: str) -> str:
    if 0 <= index_to_add < len(string):
        left_part = string[:index_to_add]
        right_part = string[index_to_add:]
        string = left_part + string_to_add + right_part
    return string


def remove_stop(string: str , from_index: int , to_index: int) -> str:
    if 0 <= from_index < len(string) and 0 <= to_index < len(string):
        left_part = string[:from_index]
        right_part = string[to_index + 1:]
        string = left_part + right_part
    return string


def switch(string: str , old_string: str , new_string: str) -> str:
    if old_string in string:
        string = string.replace(old_string, new_string)
    return string


tour_stops = input()
while True:
    command = input().split(":")
    if command[0] == "Travel":
        break
    if command[0] == "Add Stop":
        index = int(command[1])
        string = command[2]
        tour_stops = add_stop(tour_stops , index , string)
        print(tour_stops)
    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        tour_stops = remove_stop(tour_stops , start_index , end_index)
        print(tour_stops)
    elif command[0] == "Switch":
        old_string = command[1]
        new_string = command[2]
        tour_stops = switch(tour_stops , old_string , new_string)
        print(tour_stops)
print(f"Ready for world tour! Planned stops: {tour_stops}")
