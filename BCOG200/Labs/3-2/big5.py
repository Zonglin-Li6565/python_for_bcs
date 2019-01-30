import os

'''
    alter last week's big5 program so that it does everything it did last week, and in addition:
    1. reads in the questions from the five question files, and stores them in five different lists
    2. reads in and stores the scoring information from the same files
        (e.g., what questions are positive, and what questions are negative
    3. use the stored scoring information to calculate the updated score after each question is asked
    4. uses a while loop to ensure that numbers between 1-5 are the only valid responses
    5. prints the scores out in two rows and five columns, with at least 5 spaces between each columns,
        and with the score centered under the label, like this:
        openness     conscientiousness     extroversion     agreeableness     neuroticism
           20               20                  8                 5                11
'''

QUESTION_DIR: str = 'questions'

name_and_score = [
    ['openness', 8],
    ['conscientiousness', 14],
    ['extroversion', 20],
    ['agreeableness', 14],
    ['neuroticism', 38]
]

file_objects = [open(os.path.join(QUESTION_DIR, '%s.txt' % name[0]), 'r') for
                name, _ in name_and_score]

terminated = False

while not terminated:
    for i in range(len(name_and_score)):
        line = file_objects[i].readline()
        if len(line) == 0:
            terminated = True
            break
        question, weight = line.strip('\n').split(',')
        answer = int(input(question + ': '))
        while not 1 <= answer <= 5:
            print('Answer again. Be sure to answer between 1 and 5')
            answer = int(input(question + ': '))
        name_and_score[i][1] += answer * int(weight)

name_str = ''
score_str = ''

for name, score in name_and_score:
    name_str += name + ' ' * 5
    name_len = len(name)
    num_str = '%d' % score
    offset = (name_len - len(num_str)) // 2
    end = ' ' * (name_len - len(num_str) + 5 - offset)
    score_str += ' ' * offset + num_str + end

print(name_str)
print(score_str)
