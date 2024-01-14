# This is the fourth pattern problem in the series

# This problem is called the " Right-angled Repeated-Number Triangle "


n = 5  # Arbitrary value of 5 is taken

for i in range(1, n+1):
    for j in range(1, i + 1):
        print(i,end='')
    print(" ")

# Expected Output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# for n = 5

