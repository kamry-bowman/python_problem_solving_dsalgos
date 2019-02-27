def helper(height, from_pole, with_pole, to_pole):
    print(from_pole, with_pole, to_pole)
    if height >= 1:
        helper(height - 1, from_pole, to_pole, with_pole)
        move_disc(from_pole, to_pole)
        helper(height - 1, with_pole, from_pole, to_pole)


def move_disc(from_pole, to_pole):
    top_from = from_pole.pop()
    if not to_pole or top_from < to_pole[-1]:
        to_pole.append(top_from)
    else:
        raise Exception('Top ring must be small')


def hanoi(height):
    from_pole = []
    with_pole = []
    to_pole = []

    for i in range(height - 1, -1, -1):
        from_pole.append(i)

    helper(height, from_pole, with_pole, to_pole)
    print(to_pole)


hanoi(5)
