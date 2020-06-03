"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# since f(x) = 4x + 6, the equation f(a) + f(b) = f(c) - f(d) simplifies to
# a + b + d + 3 = c

# examples show cases where a = d, meaning 2a + b + 3 = c
# examples also show cases where b = d, meaning a + 2b + 3 = c

