
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


def jugs(jug1_size, jug2_size, goal):
    big_jug = jug(jug1_size)
    small_jug = jug(jug2_size)

    small_jug.pump()
    small_jug.pour(big_jug)
    small_jug.pump()
    small_jug.pour(big_jug)
    print(small_jug.fill, big_jug.fill)


jugs(4, 3, 2)
