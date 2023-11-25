import re

input_text = input()

numbers_match = re.findall(r'\d' , input_text)
cool_threshold = 0
if numbers_match:
    cool_threshold = 1
    for number in numbers_match:
        cool_threshold *= int(number)

pattern = r'([:|*]{2})([A-Z][a-z]{2,})(\1)'
matches = re.findall(pattern , input_text)
print(f"Cool threshold: {cool_threshold}")
emoji_count = len(matches)
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for match in matches:
    emoji = match[1]
    emoji_coolness = 0
    for index in range(len(emoji)):
        emoji_coolness += ord(emoji[index])
    if emoji_coolness >= cool_threshold:
        print(''.join(match))

# ['3', '1', '1', '3', '1', '1', '2', '3', '5', '2', '1']
# [('::', 'Smiley', '::'), ('**', 'Tigers', '**'), ('::', 'Mooning', '::'), ('**', 'Shy', '**')]