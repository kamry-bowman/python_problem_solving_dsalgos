from collections import namedtuple

Value = namedtuple('Value', ['item', 'weight', 'value'])

values = [
    Value(1, 2, 3),
    Value(2, 3, 4),
    Value(3, 4, 8),
    Value(4, 5, 8),
    Value(5, 9, 10)
]


def thief(capacity, values):
    values = [Value(item=x, weight=y, value=z) for (x, y, z) in values]

    items = len(values)
    table = [[None] * (capacity - 1) for i in range(items)]
    # initialize first row, looping over capacities with one item
    for i in range(capacity - 1):
        # if weight is greater than capacity, 0, else value
        value = values[0]
        cap = i + 1
        if cap >= value.weight:
            table[0][i] = [value.value, [value]]
        else:
            table[0][i] = [0, []]

    for j in range(1, len(values)):
        value = values[j]
        for i in range(capacity - 1):
            cap = i + 1
            # compare the value at at table[j - 1][i]  to table[j - 1][i - weight] + value
            max_without = table[j - 1][i][0]
            if value.weight <= i:
                max_with = table[j - 1][i - value.weight][0] + value.value
            else:
                max_with = None

            if max_with and max_with > max_without:
                old_optimum = table[j - 1][i - value.weight]
                new_optimum = [old_optimum[0] +
                               value.value, old_optimum[1] + [value]]

            else:
                new_optimum = table[j - 1][i]

            table[j][i] = new_optimum

    # for i in table:
        # print(i)
        # print('\n')
    return table[-1][-1]


print(thief(8, values))
