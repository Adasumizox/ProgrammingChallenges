from collections import deque

def dbl_linear(n):
    x, y, z = 1, deque([]), deque([])
    for _ in range(n):
        y.append(2 * x + 1)
        z.append(3 * x + 1)
        x = min(y[0], z[0])
        if x == y[0]: y.popleft()
        if x == z[0]: z.popleft()
    return x