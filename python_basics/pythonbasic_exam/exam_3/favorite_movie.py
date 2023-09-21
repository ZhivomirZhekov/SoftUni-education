points = 0
counter = 0
movie_name = ''
while True:
    movie = input()
    if movie == 'STOP':
        break
    compare = 0
    counter += 1
    for i in range(len(movie)):
        compare += ord(movie[i])
        if 64 < ord(movie[i]) < 91:
            compare -= len(movie)
        elif 96 < ord(movie[i]) < 123:
            compare -= 2 * len(movie)
        if compare > points:
            points = compare
            movie_name = movie
    if counter == 7:
        print("The limit is reached.")
        break

print(f"The best movie for you is {movie_name} with {points} ASCII sum.")