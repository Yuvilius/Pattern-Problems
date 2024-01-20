# This is the 7th pattern problem in the series

# We can call this problem simply as the "Triangle Pattern"

n = 5  # We take an arbitrary value for n

for i in range(n):
    for x in range(n - i - 1):  # Logic for printing the spaces in the pattern
        print(" ", end='')

    for y in range(2*i + 1):    # Logic for printing the stars in the pattern
        print("*", end='')

    for z in range(n - i - 1):  # Logic for printing the spaces in the pattern
        print(" ", end='')

    print("")

# Expected Outcome:
#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# for n = 5
