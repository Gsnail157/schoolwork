# Objective
# Use the class spellchecker to see what words are not spelled correctly in another file
# Compare each word using the Class method
# 1st, read the txt file and clean up the words in the txt file
from spellchecker import spellchecker

# Function to check if the file exist, if not then a exception is thrown with message


def get_file():
    y = True
    print("Welcome to Text File Spellchecker.")
    while y:
        try:
            answer = input("Enter the name of the file to read:\n")
            openfile = open(answer, 'r')
            y = False
            return openfile
        except Exception as e:
            print("Could not open file.")


if __name__ == '__main__':
    sp = spellchecker("english_words.txt")
    file_to_read = get_file()

# Counters to keep track of what line you are on and number of total and failed words
    line_counter = 0
    word_failed_count = 0
    total_words = 0
# Clean up the lines. Removes \n and seperates each word for iteration
    lines = file_to_read.readlines()
    for eachline in lines:
        eachline = eachline.rstrip()
        eachline = eachline.split()
        line_counter += 1  # Sets current line the iteration is on

        # Checks if each word is in the class object sp using the its class method.
        # If the word does not exist in the class dictionary then prints error.
        for word in eachline:
            total_words += 1
            if sp.check(word) == False:
                word_failed_count += 1
                print(
                    f'Possible Spelling Error on line {line_counter}: {word}')

    # Calculations for result
    words_passed = total_words - word_failed_count
    percent_passed = (words_passed/total_words) * 100

    # Results
    print('{:,} words passed spell checker.'.format(words_passed))
    print(f'{word_failed_count} words failed spell checker.')
    print('{:.2f}% of the words passed.'.format(percent_passed))
