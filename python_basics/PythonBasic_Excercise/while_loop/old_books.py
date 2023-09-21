# Input
searched_book = input()
checked_books = 0
founded_book = False
current_book = input()
# Logic
while current_book != 'No More Books':
    if current_book == searched_book:
        founded_book = True
        break
    checked_books += 1
    current_book = input()
# Output
if founded_book:
    print(f'You checked {checked_books} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f"You checked {checked_books} books.")