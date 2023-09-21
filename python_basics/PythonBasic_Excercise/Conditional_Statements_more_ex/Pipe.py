# Input
volume_pool_litters = int(input())
pipe1_flow_hour = int(input())
pipe2_flow_hour = int(input())
worker_absent_hours = float(input())

# Logic
pipes_flow = pipe1_flow_hour + pipe2_flow_hour
input_volume = pipes_flow * worker_absent_hours
pool_overflow = input_volume - volume_pool_litters
pool_filling_percent = input_volume / volume_pool_litters * 100
pipe1_fill_percent = ((pipe1_flow_hour * worker_absent_hours) / input_volume) * 100
# First pipe filling the pool in %
pipe2_fill_percent = ((pipe2_flow_hour * worker_absent_hours) / input_volume) * 100
# Second pipe filling pool in %
if volume_pool_litters >= input_volume:
    print(f'The pool is {pool_filling_percent:.2f}% full. Pipe 1: {pipe1_fill_percent:.2f}%. Pipe 2: {pipe2_fill_percent:.2f}%')
else:
    print(f'For {worker_absent_hours:.2f} hours the pool overflows with {pool_overflow:.2f} liters.')


