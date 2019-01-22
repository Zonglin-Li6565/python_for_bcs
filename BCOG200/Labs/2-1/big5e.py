from functools import reduce
from operator import mul, add

print('This is the Extroversion Section of the Big Five Personality Test')
print('It will help you understand why you act the way that you do and how '
      'your personality is structured.')
print('For each statement 1-50 mark how much you agree with on the scale 1-5, '
      'where:')
print('		1=disagree')
print('		2=slightly disagree')
print('		3=neutral')
print('		4=slightly agree')
print('		5=agree')

# q1 = input('Am the life of the party ')
# q6 = input('Don\'t talk a lot ')
# q11 = input('Feel comfortable around people ')
# q16 = input('Keep in the background ')
# q21 = input('Start conversations ')
# q26 = input('Have little to say ')
# q31 = input('Talk to a lot of different people at parties ')
# q36 = input('Don\'t like to draw attention to myself ')
# q41 = input('Don\'t mind being the center of attention ')
# q46 = input('Am quiet around strangers ')

# 1. convert the questions to a list
# 2. write a for loop that cycles over the list and asks each question
# 3. create an empty "answers" list
# 4. add each answer to the answer list
# 5. compute and print the persons's E score using their answer list
#    hint, you might consider using this list:
#    E_key = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]


E_key = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]

questions = [
    'Am the life of the party ',
    'Don\'t talk a lot ',
    'Feel comfortable around people ',
    'Keep in the background ',
    'Start conversations ',
    'Have little to say ',
    'Talk to a lot of different people at parties ',
    'Don\'t like to draw attention to myself ',
    'Don\'t mind being the center of attention ',
    'Am quiet around strangers ']

E_score = 0
answers = []
for i, question in enumerate(map(lambda s: s[:-1] + ': ', questions)):
    answer = int(input(question))
    while not 1 <= answer <= 5:
        print('Type in a number between 1 and 5 inclusively')
        answer = int(input(question))
    answers.append(answer)

E_score = reduce(add, map(lambda x: mul(*x), zip(E_key, answers)), 0)

print('Your E score is %d' % E_score)
