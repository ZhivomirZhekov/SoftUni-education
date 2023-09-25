number_of_snowballs = int(input())
best_snowball_weight = 0
best_snowball_time = 0
best_snowball_quality = 0
best_snowball_value = 0
for snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value = (snowball_weight / snowball_time) ** snowball_quality
    if value > best_snowball_value:
        best_snowball_value = value
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality
print(f"{best_snowball_weight} : {best_snowball_time} = "
      f"{int(best_snowball_value)} ({best_snowball_quality})")