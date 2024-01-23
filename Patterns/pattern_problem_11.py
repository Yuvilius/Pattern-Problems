# This is the 11th pattern problem in the series

n = 5  # We take an arbitrary value for n

start = 1

for i in range(n):
    if i % 2 == 0:
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start, end='')
        start = 1 - start
    print("")
