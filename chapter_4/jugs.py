import copy


class jug:
    def __init__(self, size):
        self.size = size
        self.fill = 0

    def pump(self):
        self.fill = self.size

    def empty(self):
        self.fill = 0

    def pour(self, jug):
        room = jug.size - jug.fill

        pour_amount = min(room, self.fill)

        jug.fill += pour_amount

        self.fill -= pour_amount


def did_already_visit(big_jug, small_jug, cache):
    try:
        return cache[f'{big_jug.fill}-{small_jug.fill}']
    except KeyError:
        cache[f'{big_jug.fill}-{small_jug.fill}'] = True
        return False


def save_visit(big_jug, small_jug, cache):
    cache[f'{big_jug.fill}-{small_jug.fill}'] = True


def jugs(jug1_size, jug2_size, goal):
    cache = {}

    big_jug = jug(jug1_size)
    small_jug = jug(jug2_size)

    save_visit(big_jug, small_jug, cache)

    def success(big_jug, small_jug, cache):
        if not did_already_visit(big_jug, small_jug, cache):
            result = helper(big_jug, small_jug)
            return bool(result)

    def helper(big_jug, small_jug):
        print(cache)
        if big_jug.fill == goal or small_jug.fill == goal:
            print(big_jug.fill, small_jug.fill)
            return True

        og_big_jug = copy.copy(big_jug)
        og_small_jug = copy.copy(small_jug)

        # fill big_jug
        if big_jug.fill != big_jug.size:
            big_jug.pump()
            if success(big_jug, small_jug, cache):
                return True

            # reset big_jug
            big_jug = copy.copy(og_big_jug)

        # pour out big_jug
        if big_jug.fill != 0:
            big_jug.empty()
            if success(big_jug, small_jug, cache):
                return True

            # reset big_jug
            big_jug = copy.copy(og_big_jug)

        # fill small_jug
        if small_jug.fill != small_jug.size:
            small_jug.pump()
            if success(big_jug, small_jug, cache):
                return True

            # reset small_jug
            small_jug = copy.copy(og_small_jug)

        # empty small_jug
        if small_jug.fill != 0:
            small_jug.empty()
            if success(big_jug, small_jug, cache):
                return True

            # reset small_jug
            small_jug = copy.copy(og_small_jug)

        # pour small into big_jug
        if big_jug.fill != big_jug.size and small_jug.fill != 0:
            small_jug.pour(big_jug)
            if success(big_jug, small_jug, cache):
                return True
            # reset small and big
            big_jug = copy.copy(og_big_jug)
            small_jug = copy.copy(og_small_jug)

        # pour big into small_jug
        if small_jug.fill != small_jug.size and big_jug.fill != 0:
            big_jug.pour(small_jug)
            if success(big_jug, small_jug, cache):
                return True
            # reset small and big
            big_jug = copy.copy(og_big_jug)
            small_jug = copy.copy(og_small_jug)

        save_visit(big_jug, small_jug, cache)
        return False

    helper(big_jug, small_jug)


jugs(5, 3, 2)
