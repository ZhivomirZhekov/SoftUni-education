centuries = int(input())
to_years = centuries * 100
to_days = int(to_years * 365.2422)
to_hours = to_days * 24
to_minutes = to_hours * 60
print(f"{centuries} centuries = {to_years} years = {to_days} days = {to_hours} hours = {to_minutes} minutes")
