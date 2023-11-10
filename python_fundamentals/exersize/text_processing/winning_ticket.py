def check_ticket(some_ticket):
    if len(some_ticket) != 20:
        return "invalid ticket"
    winning_symbols = ["@" , "#" , "$" , "^"]
    left_part = some_ticket[:10]
    right_part = some_ticket[10:]
    for symbol in winning_symbols:
        for uninterrupted_match_length in range(10 , 5 , -1):
            wining_symbol_repetition = symbol * uninterrupted_match_length
            if wining_symbol_repetition in left_part and wining_symbol_repetition in right_part:
                if uninterrupted_match_length == 10:
                    return f'ticket "{some_ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'
    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]
for ticket in tickets:
    print(check_ticket(ticket))
