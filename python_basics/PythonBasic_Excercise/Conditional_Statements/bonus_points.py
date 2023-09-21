#User Input

starting_points = int(input())
bonus = 0

#Logic

if starting_points < 100:
    bonus = 5
elif    starting_points > 1000:
    bonus = starting_points * 0.1
else:
    bonus = starting_points * 0.2

if starting_points % 2 ==0:
    bonus += 1
elif starting_points % 10 ==5:
    bonus += 2

final_sum = starting_points + bonus

#Output

print(bonus)
print(final_sum)
