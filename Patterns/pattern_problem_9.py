# This is the 9th pattern problem in the series

# At first sight, this pattern is the combination of the previous two patterns,
# so we'll simply call it a "diamond pattern"

n = 5  # We take an arbitrary value for n

for i in range(n):
    for x in range(n - i - 1):  # Logic for printing the spaces in the pattern
        print(" ", end='')

    for y in range(2*i + 1):    # Logic for printing the stars in the pattern
        print("*", end='')

    for z in range(n - i - 1):  # Logic for printing the spaces in the pattern
        print(" ", end='')

    print("")

for j in range(n):
    for x in range(j):                # Logic for printing the spaces in the pattern
        print(' ', end='')

    for y in range(2*n - (2*j + 1)):  # Logic for printing the stars in the pattern
        print("*", end='')

    for z in range(j):
        print(' ', end='')            # Logic for printing the spaces in the pattern

    print("")

# Expected Output:
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *
# for n = 5
