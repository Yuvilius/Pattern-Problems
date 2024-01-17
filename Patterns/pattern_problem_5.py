# This is the 5th pattern problem in the series

# This problem is called "Inverted Right Angle Triangle" Pattern

n = 5  # We take an arbitrary value of n

for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print("")

# Expected Outcome:
# * * * * *
# * * * *
# * * *
# * *
# *
# for n = 5

