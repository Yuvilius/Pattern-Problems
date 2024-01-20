# This is the 8th pattern problem in the series

# Based on the last problem, we can call this the "Inverted Triangle Pattern"

n = 5  # We take an arbitrary value for n

for i in range(n):
    for x in range(i):                # Logic for printing the spaces in the pattern
        print(' ', end='')

    for y in range(2*n - (2*i + 1)):  # Logic for printing the stars in the pattern
        print("*", end='')

    for z in range(i):
        print(' ', end='')            # Logic for printing the spaces in the pattern

    print("")

# Expected Output:
# *********
#  *******
#   *****
#    ***
#     *
# for n = 5
