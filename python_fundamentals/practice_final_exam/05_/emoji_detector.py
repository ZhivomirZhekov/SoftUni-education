import re

input_text = input()

numbers_match = re.findall(r'\d' , input_text)
cool_threshold = 1
for number in numbers_match:
    cool_threshold *= int(number)

pattern = r'(:{2}|\*{2})([A-Z][a-z]{2,})(\1)'

matches = re.finditer(pattern , input_text)
emoji_count = 0
cool_emoji = []
for match in matches:
    emoji_count += 1
    emoji = match.group()
    emoji_coolness = 0
    for index in range(len(emoji)):
        if emoji[index].isalpha():
            emoji_coolness += ord(emoji[index])
    if emoji_coolness >= cool_threshold:
        cool_emoji.append(emoji)
print(f"Cool threshold: {cool_threshold}")
print(f"{emoji_count} emojis found in the text. The cool ones are:")
for emoji in cool_emoji:
    print(emoji)
# # ['3', '1', '1', '3', '1', '1', '2', '3', '5', '2', '1']
# # [('::', 'Smiley', '::'), ('**', 'Tigers', '**'), ('::', 'Mooning', '::'), ('**', 'Shy', '**')]
# <re.Match object; span=(49, 59), match='::Smiley::'>
# <re.Match object; span=(76, 86), match='**Tigers**'>
# <re.Match object; span=(185, 196), match='::Mooning::'>
# <re.Match object; span=(197, 204), match='**Shy**'>

