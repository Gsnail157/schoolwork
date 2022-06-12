# Exersize:

sentence = "This is a common interview question"

character_frequency = {}
for character in sentence:
    if character in character_frequency:
        character_frequency[character] += 1
    else:
        character_frequency[character] = 1

char_freq_sorted = sorted(
    character_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_freq_sorted[0])

# Project

print(range(1, 100))

total_num = 0
for num in list(range(1, 100)):
    if num % 3 and 5 == 0:
        total_num += num

print(total_num)
