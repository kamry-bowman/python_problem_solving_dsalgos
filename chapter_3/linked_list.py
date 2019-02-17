class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newnext):
        self.next = newnext


class LinkedList:
    def __init__(self):
        self.head = None
        self.end = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        if self.end is None:
            self.end = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None and found == False:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            if self.end == current:
                self.end = previous
            previous.setNext(current.getNext())
            return current.getData()

    def append(self, item):
        temp = Node(item)
        if self.end is not None:
            self.end.setNext(temp)
            self.end = temp
        else:
            self.add(item)


mylist = LinkedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(3))
print(mylist.remove(17))
print(mylist.size())
mylist.append(22)
print(mylist.size())
