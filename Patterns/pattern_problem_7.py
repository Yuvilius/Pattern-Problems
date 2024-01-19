# This is the 7th pattern problem in the series

n = 5  # We take an arbitrary value for n

for i in range(n):
    for x in range(n - i - 1):
        print(" ", end='')

    for y in range(2*i + 1):
        print("*", end='')

    for z in range(n - i - 1):
        print(" ", end='')

    print("")

