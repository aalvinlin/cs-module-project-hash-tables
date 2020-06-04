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

# coin/integer partitions

# examples show cases where a = d, meaning 2a + b + 3 = c
# examples also show cases where b = d, meaning a + 2b + 3 = c

# inefficient O(n^2) approach

# store the sums and differences of each (x, y) combination
# pair_sums = dict()
# pair_differences = dict()

function_values = dict()

# store known sums and differences and the tuples that will generate them
sums_to_known_tuples = dict()
differences_to_known_tuples = dict()

for number1 in q:

    function_values[number1] = f(number1)

    for number2 in q:

        tuple_1_2 = (number1, number2)
        tuple_2_1 = (number2, number1)

        pair_sum = f(number1) + f(number2)
        pair_difference = f(number1) - f(number2)

        # y1 = f(number1)
        # y2 = f(number2)

        # # store the sum for each (x, y) combination
        # pair_sum = y1 + y2

        # pair_sums[tuple_1_2] = pair_sum
        # pair_sums[tuple_2_1] = pair_sum

        # # store the difference for each (x, y) combination
        # pair_difference = y1 - y2

        # pair_differences[tuple_1_2] = pair_difference
        # pair_differences[tuple_2_1] = -pair_difference

        # store the pairs that will generate each sum
        if pair_sum not in sums_to_known_tuples:
            sums_to_known_tuples[pair_sum] = []
        
            sums_to_known_tuples[pair_sum].append(tuple_1_2)

            # don't store the pair twice if the numbers are the same: (3, 3)
            if number1 != number2:
                sums_to_known_tuples[pair_sum].append(tuple_2_1)
        
        # store the pair for difference f(number1) - f(number2)
        if pair_difference not in differences_to_known_tuples:
            differences_to_known_tuples[pair_difference] = []

            differences_to_known_tuples[pair_difference].append(tuple_1_2)

        # store the pair for difference f(number2) - f(number1)
        if -pair_difference not in differences_to_known_tuples and number1 != number2:
            differences_to_known_tuples[-pair_difference] = []

            differences_to_known_tuples[-pair_difference].append(tuple_2_1)

# check for all values where the sum and difference are the same
shared_values = set(sums_to_known_tuples.keys()).intersection(set(differences_to_known_tuples.keys()))

# look up all tuple combinations for each sum and difference
for value in shared_values:

    known_sum_tuples = sums_to_known_tuples[value]
    known_difference_tuples = differences_to_known_tuples[value]

    for sum_tuple in known_sum_tuples:

        for difference_tuple in known_difference_tuples:

            a, b = sum_tuple
            c, d = difference_tuple

            print(f"f({a}) + f({b}) = f({c}) - f({d})    {function_values[a]} + {function_values[b]} = {function_values[c]} - {function_values[d]}")

# print(pair_sums, "\n")
# print(pair_differences, "\n")
# print(sums_to_known_tuples, "\n")
# print(differences_to_known_tuples, "\n")

# print(known_sums)
# print(known_differences)
# print(shared_values)
