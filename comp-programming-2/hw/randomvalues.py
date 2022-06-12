import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
# random number generator with the inputs you give and key
print(random.choices([1, 2, 3, 4], k=2))
# Random password generator
print(" ".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=6)))


numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
