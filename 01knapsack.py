def knapsack_recursive(weights, values, capacity, n):
    # Base case: no items left or capacity is 0
    if n == 0 or capacity == 0:
        return 0

    # If the weight of the nth item is more than the knapsack capacity, it cannot be included
    if weights[n-1] > capacity:
        return knapsack_recursive(weights, values, capacity, n-1)
    else:
        # Return the maximum of two cases:
        # (1) nth item included
        # (2) nth item not included
        return max(
            values[n-1] + knapsack_recursive(weights, values, capacity - weights[n-1], n-1),
            knapsack_recursive(weights, values, capacity, n-1)
        )

# Example usage
weights = [10,20,30]
values = [60,100,120]
capacity = 50
n = len(values)

max_value = knapsack_recursive(weights, values, capacity, n)
print(f"The maximum value that can be achieved within the given capacity is: {max_value}")
