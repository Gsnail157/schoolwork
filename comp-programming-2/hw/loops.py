# We use for loops to create repitition
# Example
# We use for loops to iterate over elements of a sequence for example if you want to repeat "n" a number of times

a = ["Apple", "Banana", "Microsoft"]

print(a[0])  # Instead of writing out each print statement, you can you a for loop
print(a[1])
print(a[2])

# Translation:

for fruits in a:  # For each element in "a", do the following.
    # This does the same exact thing as the code above. You can call this element anything
    print(fruits)  # Print each [fruit] element in the list


word = "Python"
for letter in word:
    print(letter)

successful = True

# Use a for loop to creates a range of numbers
for number in list(range(3)):   # You can make the range into a list of numbers
    print("Attempt")
for number in list(range(1, 4)):
    print("Attempt", number, number * ".")

# For...Else...Elif
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 Times")

# Nested loops

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

# Iterable

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# While Loops,
# Used to repeat a block of code. Instead of running the block code once,
# It executes the code block multiple times until a certain condition is met
# Used when you dont know what is in a list and you know if the list in order

number = 100
while number > 0:
    print(number)
    number //= 2


total2 = 0
j = 1
while j < 5:
    total2 += j
    j += 1
print(total2)


total3 = 0
for num in list(range(1, 8)):
    if num % 3 == 0:
        total3 = total3 + num

print(total3)
