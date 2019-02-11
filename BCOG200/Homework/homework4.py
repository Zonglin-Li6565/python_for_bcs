import sys
'''
    1. why doesnt the the following code work?

        my_tuple = ('dog', 'cat', 'mouse')
        my_tuple[2] = 'rat'
'''
# type your answer here
# Tuple is immutable
'''
    2. Explain the difference between what .split() and .partition() do below:

        my_string = "i like pizza"
        result1 = my_string.split(" ")
        result2 = my_string.partition(" ")
'''
# type your answer here
# Split will split the string using the deliminator
# Partition will split the string into 3 parts: before (first occurange of )
# deliminator, deliminator and after deliminator
'''
    3. What is wrong with this code?

        my_list = ['dog', 'cat', 'mouse']
        new_list = my_list.split(',')
'''
# type your answer here
# You can't split a list
'''
    4. What is wrong with this code, which is supposed to print out each letter in the list, one at a time?

        my_list_of_tuples = [('dog', 'cat', 'mouse'), ('benji', 'tom', 'jerry'), ('1', '2', '3'), ('46', '41', '16')]
    
        for i in range(3):
            for j in range(4):
                print(my_list_of_tuples[i][j])
'''
# type your answer here
# The index is wrong. And even if it's correct, the code didn't print out one letter at a time.
'''
    5. To the best of your understanding, what is happening in the following code? Comment each line, and explain
    the overall result, especially if my_dict2 and my_dict3 are the same, and why or why not?
    
    my_dict1 = {"dog": 1, "cat": 2, "mouse": 3}   # Create a dict containing three entries
    my_dict2 = my_dict1  # Create a new variable my_dict2 referring to the same dict
    my_dict3 = my_dict1.copy()  # Make a copy of the dict
    my_dict2['zebra'] = 4  # Add an entry to the original dict. Should not change my_dict3
    
'''
# type your answer here
# my_dict2 and my_dict3 are not the same. my_dict3 is a shadow copy from my_dict2. Adding a new entry in my_dict2 will not affect my_dict3
'''
    6. Write a program that reads in a file, and stores the contents of the file in a dictionary, with each line 
        being a key, and the line number of the file as the value. For example, a file that looked like this:
            dog
            cat
            mouse
        should result in the dictionary my_dict = {"dog": 1, "cat": 2, "mouse": 3}
'''
print("Output of question #6")
with open('homework4.py', 'r') as f:
    dictionary = {}
    for i, line in enumerate(f):
        dictionary[line] = i
print('\n')
''' 
    7. What does your program do if there is a duplicate word in the file?
'''
# type your answer here
# The value of that word will be the line number of the last occurance
'''
    8. Write a program that reads in a file, and stores the contents of the file in a set, with each line 
        being a member of the set. Have the program print out:
            - how many total lines were in the file
            - how many unique lines were in the file
            - how many duplicate lines were in the file
'''
print("Output of question #8")
# your code for #8 goes here
with open('homework4.py', 'r') as f:
    lines = f.readlines()
    line_set = set().union(lines)
    print('Total lines:', len(lines))
    print('Unique lines:', len(line_set))
    print('Duplicate lines:', len(lines) - len(line_set))
print('\n')
'''
    9. Write a program that reads in two files, and stores the unique words of each file in two different sets. Use
        the built in set functions to print out:
            - the number of words that are in both files
            - the number of words that are in file1 but not file2
            - the number of words that are in file2 but not file1
'''
print("Output of question #9")
# your code for #9 goes here
set1 = set()
set2 = set()

with open('homework3.py', 'r') as f:
    lines = f.readlines()
    for line in lines:
        set1.update(line.split(' '))

with open('homework4.py', 'r') as f:
    lines = f.readlines()
    for line in lines:
        set2.update(line.split(' '))

intersection = set1.intersection(set2)
in1_not_2 = set1.difference(set2)
in2_not_1 = set2.difference(set1)
print('Num of words in both files:', len(intersection))
print('Num of words in file1 but not file2:', len(in1_not_2))
print('Num of words in file2 but not file1:', len(in2_not_1))

print('\n')
'''
    10. Write a program that:
        - reads in a file, uses a dictionary to count the frequency of all the words in the file
        - takes an integer as an sys.argv input argument
        - prints out the n most frequent words in the file, where n is the number entered as a sys.argv argument
'''
print("Output of question #10")
# your code for #10 goes here
if len(sys.argv) != 2 or not sys.argv[1].isdigit():
    print('Invalid argument')
    exit(1)
n = int(sys.argv[1])
with open('homework4.py', 'r') as f:
    counter = {}
    lines = f.readlines()
    for line in lines:
        words = line.split(' ')
        for word in words:
            if not word in counter:
                counter[word] = 0
            counter[word] += 1
    list_of_tuples = list(counter.items())
    list_of_tuples.sort(key=lambda t: t[1], reverse=True)
    for i in range(min(len(list_of_tuples), n)):
        print(list_of_tuples[i][0])

print('\n')
