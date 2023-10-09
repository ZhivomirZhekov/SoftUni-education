people_waiting_for_lift = int(input())
current_state_of_lift = [int(i) for i in input().split()]
end_state_of_lift = []
for wagon in range(len(current_state_of_lift)):
    people_to_fill_wagon = min(4 - current_state_of_lift[wagon] , people_waiting_for_lift)
    people_waiting_for_lift -= people_to_fill_wagon
    current_state_of_lift[wagon] += people_to_fill_wagon

if min(current_state_of_lift) < 4:
    print(f'The lift has empty spots!')
elif people_waiting_for_lift > 0:
    print(f"There isn't enough space! {people_waiting_for_lift} people in a queue!")
print(' '.join([str(i) for i in current_state_of_lift]))


