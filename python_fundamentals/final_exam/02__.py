import re
text_string = input()

pattern = r"[@|#]+([a-z]{3,})[@|#]+\W*\/+(\d+)\/+"

matches = re.findall(pattern , text_string)

for match in matches:
    color = match[0]
    amount = match[1]
    print(f"You found {amount} {color} eggs!")
