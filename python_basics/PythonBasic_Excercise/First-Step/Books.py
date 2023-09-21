No_pages = int(input())
pages_per_hour = int(input())
days = int(input())
pages_per_day = No_pages/pages_per_hour
hour_per_day = pages_per_day/days
print(round(hour_per_day))

