def dp_knapsack(items, max_time):
    n = len(items)
    B = [[0] * (max_time + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for t in range(1, max_time + 1):
            if items[i-1][0] <= t:
                B[i][t] = max(B[i-1][t], B[i-1][t - items[i-1][0]] + items[i-1][1])
            else:
                B[i][t] = B[i-1][t]

    x = [0] * n
    i, k = n, max_time
    max_pts = B[n][max_time]

    while i > 0 and k > 0:
        if B[i][k] != B[i-1][k]:
            x[i-1] = 1
            k -= items[i-1][0]
        i -= 1

    return max_pts, x

# Input and usage
max_time = int(input("Enter the max time: "))
n = int(input("Enter the number of questions: "))
items = [tuple(map(int, input("Enter time and points: ").split())) for _ in range(n)]

max_pts, solution_vector = dp_knapsack(items, max_time)

print("The max points is:", max_pts)
print("The solution vector is:", solution_vector)
