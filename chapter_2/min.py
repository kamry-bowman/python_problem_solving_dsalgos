def min_quadratic(list):
    min = list[0]
    for i in list:
        new_small = True
        for j in list:
            if i > j:
                new_small = False
        if new_small:
            min = i
    return min


def min_linear(list):
    min = list[0]
    for i in list:
        if i <= min:
            min = i
    return min


a_list = [4, 8, 9, 7, 88, 73, 23, 1, 3, 5]

print(min_quadratic(a_list))
print(min_linear(a_list))
