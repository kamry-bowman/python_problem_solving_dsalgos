from collections import deque
from random import randrange
from time import time

MAX_ITEMS = 30
CUSTOMER_PER_MINUTE = 3
NUM_REGISTERS = 2
ITEM_SCAN_TIME = 1


class Register:
    def __init__(self):
        self.line = deque()
        self.current = None
        self.history = []

    def add(self, customer):
        self.line.appendleft(customer)

    def tick(self, time):
        if self.current:
            self.current.process()
            if not self.current.items:
                self.history.append(time - self.current.start)
                self.current = None
        elif self.line:
            next = self.line.pop()
            self.current = next


class Customer:
    def __init__(self, start):
        self.items = randrange(1, MAX_ITEMS)
        self.start = start
        self.current = 0

    def process(self):
        if not self.current and self.items > 0:
            self.items -= 1
            self.current = ITEM_SCAN_TIME
        else:
            self.current -= 1


def simulate(minutes=60):

    seconds = minutes * 60
    customer_rate = int(60 / CUSTOMER_PER_MINUTE)
    registers = [Register() for i in range(NUM_REGISTERS)]

    for second in range(seconds):
        draw = randrange(0, customer_rate)
        if draw == 0:
            customer = Customer(second)
            lowest = registers[0]
            for register in registers:
                if len(register.line) < len(lowest.line):
                    lowest = register
            lowest.add(customer)
        for register in registers:
            register.tick(second)

    still_waiting = 0
    total_customers = 0
    total_wait = 0
    for register in registers:
        still_waiting += len(register.line)
        for item in register.history:
            total_customers += 1
            total_wait += item
    print(
        f'still waiting: {still_waiting}, average wait: {total_wait / total_customers / 60:.2f}')


simulate()
