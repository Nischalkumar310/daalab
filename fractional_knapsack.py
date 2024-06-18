class Item:
    def __init__(self,price,weight):
        self.price = price
        self.weight = weight
        self.x = 0
def fractional_knapsack(items,capacity):
    items.sort(key = lambda item : item.price / item.weight, reverse = True)
    total_profit = 0
    for item in items:
        if capacity >= item.weight:
            item.x = 1
            capacity -= item.weight
            total_profit += item.price
        else:
            fraction = capacity / item.weight
            item.x = fraction
            total_profit += item.price * fraction
            break
    return total_profit, [item.x for item in items]
n = int(input())
items = []
for _ in range(n):
    price = int(input())
    weight = int(input())
    items.append(Item(price,weight))
capacity = int(input())
max_profit, result_vector = fractional_knapsack(items,capacity)
print(max_profit)
print(result_vector)