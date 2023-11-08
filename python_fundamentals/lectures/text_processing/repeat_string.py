text = input().split()

new_tex = [txt * len(txt) for txt in text]

print(''.join(new_tex))
