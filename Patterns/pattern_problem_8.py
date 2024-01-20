# This is the 8th pattern problem in the series

n = 5  # We take an arbitrary value for n

for i in range(n):
    for x in range(i):
        print(' ', end='')

    for y in range(2*n - (2*i + 1)):
        print("*", end='')

    for z in range(i):
        print(' ', end='')

    print("")
