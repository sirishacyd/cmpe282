def array_manipulation(n, queries):
    arr = [0] * (n + 1)

    for query in queries:
        a, b, k = query
        arr[a-1] += k
        arr[b] -= k

    max_value = 0
    current_sum = 0

    for i in arr:
        current_sum += i
        max_value = max(max_value, current_sum)

    return max_value
