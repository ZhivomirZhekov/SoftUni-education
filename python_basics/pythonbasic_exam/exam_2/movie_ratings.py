# Input
number_movies = int(input())
# Logic
highest = 0
highest_movie = ''
lowest = 0
lowest_movie = ''
compare = 0
total = 0
for i in range(number_movies):
    name_movie = input()
    rating_movie = float(input())
    total += rating_movie
    if i == 0:
        highest = rating_movie
        lowest = rating_movie
        highest_movie = name_movie
        lowest_movie = name_movie
    if rating_movie > highest:
        highest = rating_movie
        highest_movie = name_movie
    if rating_movie < lowest:
        lowest = rating_movie
        lowest_movie = name_movie
# Output
average = total / number_movies
print(f"{highest_movie} is with highest rating: {highest:.1f}")
print(f"{lowest_movie} is with lowest rating: {lowest:.1f}")
print(f"Average rating: {average:.1f}")