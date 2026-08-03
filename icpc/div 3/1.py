t = int(input("enter no.of tasks"))  # number of test cases

for _ in range(t):
    n = int(input("enter length of array"))  # size of array
    arr = list(map(int, input("array").split()))

    zeros = arr.count(0)
    negs = arr.count(-1)

    # Step 1: turn all zeros into 1 (each costs 1 operation)
    ops = zeros

    # Step 2: if negatives count is odd
    if negs % 2 == 1:
        ops+=2

    print(ops)
