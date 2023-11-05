exam_results = {}
exam_submissions = {}
while True:
    attendees = input()
    if 'finished' in attendees:
        break
    if 'banned' in attendees:
        user_name, command = attendees.split('-')
        for attendee in exam_results.values():
            if user_name in attendee.keys():
                attendee[user_name] = 'banned'
    else:
        user_name , language , points = attendees.split('-')
        if language not in exam_results:
            exam_results[language] = {}
            exam_results[language][user_name] = int(points)
            exam_submissions[language] = 0
        elif user_name not in exam_results[language]:
            exam_results[language][user_name] = int(points)

        elif exam_results[language][user_name] < int(points):
            exam_results[language][user_name] = int(points)
        exam_submissions[language] += 1


print("Results:")
for language, attendees in exam_results.items():
    for user_name , score in attendees.items():
        if score != 'banned':
            print(f"{user_name} | {score}")
print("Submissions:")
for language, attendees_counted in exam_submissions.items():
    print(f"{language} - {attendees_counted}")

