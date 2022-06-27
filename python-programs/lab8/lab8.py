from birthday import *


def main():
    # Create lists
    cleanlist = []
    hashtable = []
    for i in range(12):
        hashtable.append([])

    # Open file and read the data
    try:
        file = open('bdaylist.txt', 'r')
        lines = file.readlines()
    except Exception as e:
        print("Could not open File!")
        return

    # Clean the Data
    for line in lines:
        x = line.strip('\n')
        y = x.split("/")
        cleanlist.append(y)

    # Hash file list and add to hash table
    for date in cleanlist:
        x = Birthday(date[0], date[1], date[2])
        y = hash(x)
        hashtable[y].append(x)

    # Print Results
    for i in range(12):
        print(f'Hash location {i} has {len(hashtable[i])} in it')


if __name__ == '__main__':
    main()
