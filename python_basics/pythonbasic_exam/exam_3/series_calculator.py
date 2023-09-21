sitcom_name = input()
seasons = int(input())
episodes = int(input())
time_episode = float(input())

total_time_need = seasons * 10 + seasons * episodes * time_episode * 1.2
print(f"Total time needed to watch the {sitcom_name} series is {round(total_time_need)} minutes.")