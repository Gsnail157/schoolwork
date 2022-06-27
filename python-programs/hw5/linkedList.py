class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, data):
        self.data = data

    def setNext(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        mystr = ''
        current = self.head

        while current != None:
            mystr += str(current.getData())
            current = current.getNext()

        return mystr

    def __len__(self):
        if self.head == None:
            return 0  # if list is empty return 0

        current = self.head  # list is not empty and has at least 1 Node
        counter = 1

        while current.getNext() != None:
            counter += 1
            current = current.getNext()
        return counter

    def __getitem__(self, index):
        if index > len(self):
            raise IndexError

        current = self.head

        for i in range(index):
            current = current.getNext()

        if current == None:
            return
        else:
            return current.getData()

    def isEmpty(self):
        return self.head == None

    def search(self, data):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()

        return found

    def append(self, data):
        newNode = Node(data)

        if self.isEmpty():       # if list is empty, head will point to newNode
            self.head = newNode

        else:                     # list is not empty, go to end of list and add newNode there
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newNode)

    def remove(self, data):
        current = self.head
        previous = None
        found = False

        # first find item in the list
        while not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:  # item was in the fist node
            self.head = current.getNext()
        else:  # item was somewhere after the first node
            previous.setNext(current.getNext())
