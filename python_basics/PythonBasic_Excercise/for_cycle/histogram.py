# Input
count_number = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
# Logic
for i in range(count_number):
    input_numb = int(input())
    if input_numb < 200:
        p1 += 1
    elif input_numb < 400:
        p2 += 1
    elif input_numb < 600:
        p3 += 1
    elif input_numb < 800:
        p4 += 1
    elif input_numb >= 800:
        p5 += 1

p1_percent = p1/count_number * 100
p2_percent = p2/count_number * 100
p3_percent = p3/count_number * 100
p4_percent = p4/count_number * 100
p5_percent = p5/count_number * 100

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')