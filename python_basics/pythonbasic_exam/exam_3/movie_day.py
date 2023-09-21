time_pictures = int(input())
number_scenes = int(input())
scene_length = int(input())

preparation = time_pictures * 0.15
time = time_pictures - (number_scenes * scene_length + preparation)

if time >= 0 :
    print(f"You managed to finish the movie on time! You have {round(time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {abs(round(time))} minutes.")

