# Input
period = int(input())
# Logic
doctors = 7
treated_patients = 0
untreated_patients = 0
for i in range(1, period+1):
    patients = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if patients > 7:
        treated_patients += doctors
        untreated_patients += patients - doctors
    elif doctors >= patients:
        treated_patients += patients

# Output
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')