# Lists
# [] is used to define a list or group of objects
# We can use list and range function to create a list of numbers

# ADding and Removing items in list

from collections import deque
letters = ["a", "b", "c"]
# Add
letters.append("d")  # Add infront of list
letters.insert(0, "-")  # Add anywhere with index

# Remove
letters.pop(0)  # Pop can only remove one item
letters.remove("b")
del letters[0:3]  # del can remove a range of items
letters.clear()
print(letters)

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])

print(prices)

# Combining Lists

list1 = [1, 2, 3]
list2 = [10, 20, 30]
# If the object is iterable, then use the built in list function to make it into a list
# Use Zip Function to combine two lists together
print(list(zip(list1, list2)))  # The object created in the new list are tuples

# Stacks - LIFO (Last in first out)

#   browsing_session = []
#   browsing_session.append(1)  # Add to a Stack
#   browsing_session.pop(1)  # Remove from a stack
#   if not browsing_session:  # You need this to see if an item exist in the stack or an error will occur
#   browsing_session[-1]  # Find an item in the stack

# Queues/ More efficient to dequeue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("Empty")

#   Swapping Variables
x = 10
y = 11

x, y = y, x

print(x)
print(y)

# Sets
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second)   # Cannnot access an item with index for sets
print(first & second)   # Unordered
print(first - second)
print(first ^ second)

if 1 in first:
    print("Yes")

# Dictionaries - Look up table
# Used when working with key value pairs, key are commonly strings or numbers
# Uses {}

d = {}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 40
d[10] = 100
print(d)

# How to iterate over key-value pairs?
for key, value in d.items():
    print("Key:")
    print(key)
    print("Value:")
    print(value)
    print(" ")

point = {"x": 1, "y": 2}  # Uses Key
point = dict(x=1, y=2)
# You cannot use an index to find an object, Must use the key word
print(point["x"])
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)

#   Unpacking Operator

these_numbers = [1, 2, 3]
print(*these_numbers)
