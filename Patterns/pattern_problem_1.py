# This is the first pattern problem in the series.

# This problem is called the "Solid Square" pattern problem.

# Solution :

n = 5  # Arbitrary Value of n is taken

for i in range(n):
    for j in range(n):
        print("*", end="")   # 'end' is a python parameter used to get the output in a single line
    print()

# Expected Outcome:
# *****
# *****
# *****
# *****
# *****
# for n = 5
