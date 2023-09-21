movie_name = input()
number_days = int(input())
number_tickets = int(input())
price_tickets = float(input())
percent_cinema = int(input())

money = number_days * number_tickets * price_tickets
income = money - money * percent_cinema / 100
print(f"The profit from the movie {movie_name} is {income:.2f} lv.")