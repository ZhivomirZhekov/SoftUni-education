string = input()
uppercase_list = []
for idx in range(len(string)):
    if string[idx].isupper():
        uppercase_list.append(idx)
print(uppercase_list)