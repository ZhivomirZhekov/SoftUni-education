import re

data = input()
pattern = r'(#|@)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
result = re.findall(pattern , data)
mirror_word = []
words_count = len(result)
for pair in result:
    if pair[1] == pair[3][::-1]:
        mirror_word.append(f'{pair[1]} <=> {pair[3]}')

if words_count > 0:
    print(f'{words_count} word pairs found!')
    if not mirror_word:
        print('No mirror words!')
    else:
        print('The mirror words are:')
        print(', '.join(mirror_word))
else:
    print('No word pairs found!')
    print('No mirror words!')
