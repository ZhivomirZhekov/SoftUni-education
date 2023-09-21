# Input
rent = int(input())
statuettes = rent * 0.7
catering = statuettes * 0.85
sounding = catering * 0.5
total_send = rent + statuettes + catering + sounding
print(f'{total_send:.2f}')