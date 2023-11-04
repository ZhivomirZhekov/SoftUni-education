company_and_ids_dict = {}

while True:
    command = input()
    if command == "End":
        break
    is_not_in_company = True
    company , employee_id = command.split(" -> ")
    if company not in company_and_ids_dict.keys():
        company_and_ids_dict[company] = []
    for employees_ids in company_and_ids_dict[company]:
        if employee_id == employees_ids:
            is_not_in_company = False
            break
    if is_not_in_company:
        company_and_ids_dict[company].append(employee_id)

for company , employee_ids in company_and_ids_dict.items():
    print(f"{company}")
    for employee_id in employee_ids:
        print(f"-- {employee_id}")
