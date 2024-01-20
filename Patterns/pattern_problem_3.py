# This is the third pattern problem in the series

# This problem is called the " Right-angled Number Triangle "

n = 5  # Arbitrary value of n is taken

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print("")

# Expected Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# for n = 5
