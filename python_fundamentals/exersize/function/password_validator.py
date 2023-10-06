def password_validator(some_password: str) -> list:
    list_of_errors = []
    if len(some_password) < 6 or len(some_password) > 10:
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    counter_digits = 0
    for character in some_password:
        if character.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
validated_pass = password_validator(password)
if len(validated_pass) == 0:
    print("Password is valid")
else:
    print("\n".join(validated_pass))
