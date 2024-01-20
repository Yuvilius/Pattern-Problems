# This is the 6th pattern problem in the series

# This pattern is called "Inverted Right Angled Number Triangle"

n = 5  # We take an arbitrary value of n

for i in range(n):
    for j in range(1, n-i+1):
        print(j, end="")
    print("")

# Expected Output:
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# for n = 5
