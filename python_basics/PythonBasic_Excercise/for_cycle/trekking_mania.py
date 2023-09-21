# Input
group_climbers = int(input())
musalla = 0
monblanc = 0
kilimandjaro = 0
k2 = 0
everest = 0
total_climbers = 0
# Logic
for i in range(group_climbers):
    group_volume = int(input())
    total_climbers += group_volume
    if group_volume < 6:
        musalla += group_volume
    elif group_volume < 13:
        monblanc += group_volume
    elif group_volume < 26:
        kilimandjaro += group_volume
    elif group_volume < 41:
        k2 += group_volume
    else:
        everest += group_volume

percent_musala = musalla / total_climbers * 100
percent_monblanc = monblanc / total_climbers * 100
percent_kilimandjaro = kilimandjaro / total_climbers * 100
percent_k2 = k2 / total_climbers * 100
percent_everest = everest / total_climbers * 100
# Output
print(f'{percent_musala:.2f}%')
print(f'{percent_monblanc:.2f}%')
print(f'{percent_kilimandjaro:.2f}%')
print(f'{percent_k2:.2f}%')
print(f'{percent_everest:.2f}%')
