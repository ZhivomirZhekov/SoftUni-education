# Input
movie_name = input()
type_room = input()
number_bought_tickets = int(input())
# Logic
income_from_movie = 0
if movie_name == 'A Star Is Born':
    if type_room == 'normal':
        income_from_movie = number_bought_tickets * 7.5
    elif type_room == 'luxury':
        income_from_movie = number_bought_tickets * 10.5
    elif type_room == 'ultra luxury':
        income_from_movie = number_bought_tickets * 13.5
elif movie_name == 'Bohemian Rhapsody':
    if type_room == 'normal':
        income_from_movie = number_bought_tickets * 7.35
    elif type_room == 'luxury':
        income_from_movie = number_bought_tickets * 9.45
    elif type_room == 'ultra luxury':
        income_from_movie = number_bought_tickets * 12.75
elif movie_name == 'Green Book':
    if type_room == 'normal':
        income_from_movie = number_bought_tickets * 8.15
    elif type_room == 'luxury':
        income_from_movie = number_bought_tickets * 10.25
    elif type_room == 'ultra luxury':
        income_from_movie = number_bought_tickets * 13.25
elif movie_name == 'The Favourite':
    if type_room == 'normal':
        income_from_movie = number_bought_tickets * 8.75
    elif type_room == 'luxury':
        income_from_movie = number_bought_tickets * 11.55
    elif type_room == 'ultra luxury':
        income_from_movie = number_bought_tickets * 13.95

print(f"{movie_name} -> {income_from_movie:.2f} lv.")