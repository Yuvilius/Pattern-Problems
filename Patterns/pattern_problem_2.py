# This is the second pattern problem in the series

# This problem is called the " Right-angled triangle pattern "

n = 5  # Arbitrary value of n is taken

for i in range(n):
    for j in range(i + 1):
        print("*", end="")
    print("")

# Expected Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# for n = 5

