def solve():
    left_side = {'c': 3, 'm': 3}
    right_side = {'c': 0, 'm': 0}
    boat_left = True
    cache = {
        f'left: {left_side}, right: {right_side}, boat_left: {boat_left}': True}
    moves = [f'left: {left_side}, right: {right_side}, boat_left: {boat_left}']

    def invariant_violation(left_side, right_side):
        if left_side['m'] and left_side['c'] > left_side['m']:
            return True
        if right_side['m'] and right_side['c'] > right_side['m']:
            return True

        return False

    boat_fills = [[1, 0], [2, 0], [1, 1], [0, 1], [0, 2]]

    iterat = 0

    def helper(left_side, right_side, boat_left):
        nonlocal iterat
        iterat += 1

        # exit condition
        if right_side['c'] == 3 and right_side['m'] == 3:
            return moves

        # determine legal actions based on current state
        # try each action and call helper recursively
        # if success, return result, else continue
        boat_m = left_side['m'] if boat_left else right_side['m']
        boat_c = left_side['c'] if boat_left else right_side['c']

        for send_m, send_c in [pair for pair in boat_fills if pair[0] <= boat_m and pair[1] <= boat_c]:

            left_possibility = left_side.copy()
            right_possibility = right_side.copy()
            if boat_left:
                source = left_possibility
                target = right_possibility
            else:
                source = right_possibility
                target = left_possibility

            source['m'] -= send_m
            target['m'] += send_m
            source['c'] -= send_c
            target['c'] += send_c
            new_boat_left = not boat_left

            id = f'left: {left_possibility}, right: {right_possibility}, boat_left: {new_boat_left}'
            try:
                cache[id]
            except KeyError:
                cache[id] = True
                moves.append(id)

                if not invariant_violation(
                    left_possibility, right_possibility
                ) and helper(
                        left_possibility, right_possibility, new_boat_left
                ):
                    return moves
                else:
                    moves.pop()

        return False

    return helper(left_side, right_side, boat_left)


result = solve()
for line in result:
    print(line)
