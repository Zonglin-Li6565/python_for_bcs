import os

'''
    1. what happens if you try to open a file that is already open? type your answer as a comment.
'''
# That's fine


''' 
    2. how do you only read the first 10 characters of a file? type your answer as working python code in the space
        indicated below.    
'''
# type your answer here

with open(os.path.realpath(__file__), 'r') as f:
    print(f.read(10))

''' 
    3. Describe the difference behavior between the two following lines of code:
      if not (x > 3) or (y > 3):
      if not ((x > 3) or (y > 3)):  
'''
# In the first case, the not will be associated with (x > 3)
# In the second case, the not will be associated with ((x > 3) or (y > 3))


''' 
    4.  Can you use 'break' and 'continue' with for loops, or just with while loops?
'''
# You can use break and continue with both


''' 
   5. if you want to remove the 3rd item from a list, what is the one line of python code to do that
'''
a = [1, 2, 3, 4, 5]
a.pop(2)

''' 
    6. Write a program that asks for the temperature, and asks if it is in C or F, and converts it to the other 
        and prints it out.
'''


def read_digit(prmpt):
    val = input(prmpt)
    while not val.isdigit():
        print('Need to be a number')
        val = input(prmpt)
    return val


print("Output of question #6")
temp = read_digit('temperature')
temp = float(temp)
unit = input('unit')
while not (unit in ['C', 'F']):
    print('Only C or F')
    unit = input('unit')
if unit == 'C':
    print(temp * 9 / 5 + 32)
else:
    print((temp - 32) * 5 / 9)

''' 
    7. Write a program that will compute the area of a circle. 
    Prompt the user to enter the radius and print a nice message back to the user with the answer.
'''
print("Output of question #7")
radius = read_digit('radius?')
radius = float(radius)
print('Nice circle area: %.02f' % (3.14 * radius ** 2))

print()

''' 
    8.  It is possible to name the days 0 through 6 where day 0 is Sunday and day 6 is Saturday.
        If you go on a wonderful holiday leaving on day number 3 (a Wednesday) and you return home after 10 nights. 
    Write a general version of the program which asks for the starting day number, and the length of your stay, 
    and it will tell you the number of day of the week you will return on.
'''
print("Output of question #8")
day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
init_day = read_digit('Start day?')
init_day = int(init_day)

duration = read_digit('Duration?')
duration = int(duration)

print(day[(init_day + duration) % len(day)])

print()

'''
    9.  write code that reads in file 'test_file2.txt', creates a separate file for each geographic region 
        the animals are from, and prints only the animals from that region to the file, one animal per line.
        for example, you should create the file 'africa.txt', and that file should have:
        
        elephant
        lion
        giraffe
        zebra
        hyena
        
        also, the program cannot "hard code" the names of the files. You need to figure out the names of the output 
        files from the input files. For example, if I test your code on a new input file that has animals from china, or
        antarctica, or Wonderland, the program should still work!
'''
print("Output of question #9")
# your code for #9 goes here
regions = {}
with open('test_file2.txt', 'r') as f:
    for line in f:
        # animal, region = tuple(map(lambda s: s.strip(), line.split(',')))
        animal = line.strip().split(',')[0]
        region = line.strip().split(',')[1]
        if not (region in regions):
            regions[region] = []
        regions[region].append(animal)

for region in regions.keys():
    with open('%s.txt' % region, 'w') as f:
        for animal in regions[region]:
            f.write(animal + '\n')
print()

'''
    10. write code that:
        1.) takes 'test_file1.txt' as input
        2.) stores each line in list
        3.) uses a for loop to iterate over that list
        4.) uses a second for loop to iterate over each word in each sentence
        5.) uses a while loop to iterate over each letter in the word, until there are no more letters in the word
        6.) prints out the document, one letter at a time, with each word on a different line and each letter separated
                by a space. For example, the first three lines should be:
                
                T h e
                g r i z z l y
                b e a r
'''
print("Output of question #10")
# your code for #10 goes here
with open('test_file1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        for word in line.split(' '):
            i = 0
            while i < len(word):
                print(word[i], end=' ')
                i += 1
            print()
print()
