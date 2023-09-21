# Input
account = input()
password = input()
while True:
    type_password = input()
    if type_password == password:
        print(f'Welcome {account}')
        break
