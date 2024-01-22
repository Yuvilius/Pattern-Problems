# This is the 10th pattern problem in the series

# Let's call this a "Pyramid Pattern"

n = 5  # We take an arbitrary value of n

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print("")

for j in range(n):
    for x in range(n-j-1):
        print("*", end='')
    print("")

# Expected Output:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
# for n = 5
