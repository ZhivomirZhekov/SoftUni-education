import re

text = input()
pattern = r"(#|@)([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1"

matches = re.findall(pattern , text)

mirror_words = []
for match in matches:
    word1 = match[1]
    word2 = match[2]
    if word1[::-1] == word2:
        to_append = f"{word1} <=> {word2}"
        mirror_words.append(to_append)

if len(matches) > 0:
    valid_pairs_count = len(matches)
    print(f"{valid_pairs_count} word pairs found!")
    if not mirror_words:
        print("No mirror words!")
    else:

        print("The mirror words are:")
        print(", ".join(mirror_words))
else:
    print("No word pairs found!")
    print("No mirror words!")
