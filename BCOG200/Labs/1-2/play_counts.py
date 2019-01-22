# write a program where you have to input the name and play count for each
# justin bieber song, and store them in separate variables
# print each song next to its play count
# print out the total play count for all justin bieber songs added together

total = 0

while True:
    name_and_count = input('Name and count: ')
    if len(name_and_count) == 0:
        print('total: %d' % total)
        break
    _, count = name_and_count.split()
    total += int(count.strip())
