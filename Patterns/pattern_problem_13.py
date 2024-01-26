# This is the 13th pattern problem in the series

n = 5  # We take an arbitrary value of n

num = 1

for i in range(1, n+1):
    for j in range(1, i+1):
        print(num, end='')
        num += 1
    print("")
