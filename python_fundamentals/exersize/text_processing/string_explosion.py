string = input()
final_string = ""
explosion = 0

for index in range(len(string)):
    if string[index] != ">" and explosion > 0:
        explosion -= 1
    elif string[index] == ">":
        final_string += string[index]
        explosion += int(string[index + 1])
    else:
        final_string += string[index]
print(final_string)
