a1 = int(input())
a2 = int(input())
n = int(input())
n_2 = n / 2
from math import floor
for i in range(a1, a2):
    for j in range(1, n):
        for k in range(1, floor(n_2)):
            p = i + j + k
            if i % 2 != 0 and p % 2 != 0:
                print(f"{chr(i)}-{j}{k}{i}")

