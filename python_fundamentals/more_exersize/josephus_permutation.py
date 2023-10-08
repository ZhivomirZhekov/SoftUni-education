list_of_people = input().split()
execution_number = int(input())
executed_people_list = []
index_executed = 0

while len(list_of_people) > 0:
    index_executed = (execution_number - 1 + index_executed) % len(list_of_people)
    executed_people_list.append(list_of_people.pop(index_executed))
print(f"[{','.join(executed_people_list)}]")

