from pythonds.basic.queue import Queue

import random


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 11)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." %
          (averageWait, printQueue.size()))

# (10 students / 1 hour) * (2 tasks / 1 student) * (1 hour / 60 minutes) * (1 minute / 60 seconds) = 1 task / 180 seconds
# (20 students / 1 hour) * (2 tasks / 1 student) * (1 hour / 60 minutes) * (1 minute / 60 seconds) = 1 task / 90 seconds


def newPrintTask():
    num = random.randrange(1, 91)
    if num == 90:
        return True
    else:
        return False


for i in range(10):
    simulation(3600, 5)
