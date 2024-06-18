def g(vertex, rem_v):
    if not rem_v:
        return memo[vertex]
    mi = float('inf')
    for i in rem_v:
        temp = rem_v.copy()
        temp.remove(i)
        val = w[vertex][i] + g(i, temp)
        if val < mi:
            mi = val
            index[(vertex, tuple(rem_v))] = i
    memo[(vertex, tuple(rem_v))] = mi
    return mi

def path(vertex, rem_v):
    r = [vertex + 1]
    while rem_v:
        next_vertex = index[(vertex, tuple(rem_v))]
        r.append(next_vertex + 1)
        rem_v.remove(next_vertex)
        vertex = next_vertex
    r.append(1)
    return r

v = int(input('Number of objects: '))
w = [list(map(int, input(f'{i+1}->').split(','))) for i in range(v)]

memo = {i: w[i][0] for i in range(1, v)}
index = {}

min_cost = g(0, list(range(1, v)))
required_path = path(0, list(range(1, v)))

print("The min cost:", min_cost)
print("The required path is:", required_path)
