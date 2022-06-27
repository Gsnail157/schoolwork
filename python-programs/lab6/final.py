class Stack:
    # Create a New Empty Stack
    def __init__(self):
        self.__S = []

    # Display the Stack
    def __str__(self):
        return str(self.__S)

    # Add a new element to top of stack
    def push(self, x):
        self.__S.append(x)

    # Remove the top element from stack
    def pop(self):
        return self.__S.pop()

    # See what element is on top of stack
    # Leaves stack unchanged
    def top(self):
        return self.__S[-1]

    def isEmpty(self):
        return len(self.__S) == 0


class Queue():
    def __init__(self):
        self.__theList = []

    def __str__(self):
        return str(self.__theList)

    def put(self, item):
        self.__theList.append(item)

    def get(self):
        a = self.__theList.pop(0)
        return a

    def clear(self):
        self.__theList = []

    def empty(self):
        if len(self.__theList) == 0:
            return True
        else:
            return False


queue = Queue()
stack = Stack()

word = 'racercar'

for letter in word:
    queue.put(letter)
    stack.push(letter)

print(word)
if queue.get() == stack.top():

    print("Yes")
else:

    print("No")

