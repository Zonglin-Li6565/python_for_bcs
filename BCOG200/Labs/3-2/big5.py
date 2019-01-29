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

QUESTION_DIR = 'questions'


def ask_and_score(file_path: str, init_val: int) -> int:
    with open(file_path, 'r') as f:
        lines = list(map(lambda s: s.strip('\n').split(','), f.readlines()))
        total = init_val
        for question, weight in lines:
            answer = int(input(question + ': '))
            while not 1 <= answer <= 5:
                print('Answer again. Be sure to answer between 1 and 5')
                answer = int(input(question + ': '))
            total += answer * int(weight)
    return 0


val_map = {
    'O': 8,
    'C': 14,
    'E': 20,
    'N': 38,
    'A': 14,
}

for category in val_map.keys():
    score = ask_and_score(
        os.path.join(QUESTION_DIR, '%s.txt' % category.lower()),
        val_map[category])

print('openness     conscientiousness     extroversion     agreeableness     '
      'neuroticism')
print('   %02d               %02d                  %02d               %02d   '
      '             %02d' % (val_map['O'],
                             val_map['C'],
                             val_map['E'],
                             val_map['A'],
                             val_map['N']))
