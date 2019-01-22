import os

if not os.path.isfile('big5_summary.txt'):
    print('Missing big5_summary.txt')
    exit(0)

print('This is the Big Five Personality Test')
print(
    'It will help you understand why you act the way that you do and how your '
    'personality is structured.')
print(
    'For each statement 1-50 mark how much you agree with on the scale 1-5, '
    'where:')
print('		1=disagree')
print('		2=slightly disagree')
print('		3=neutral')
print('		4=slightly agree')
print('		5=agree')

q1 = int(input('Am the life of the party '))
q2 = int(input('Feel little concern for others '))
q3 = int(input('Am always prepared '))
q4 = int(input('Get stressed out easily '))
q5 = int(input('Have a rich vocabulary '))
q6 = int(input('Don\'t talk a lot '))
q7 = int(input('Am interested in people '))
q8 = int(input('Leave my belongings around '))
q9 = int(input('Am relaxed most of the time '))
q10 = int(input('Have difficulty understanding abstract ideas '))
q11 = int(input('Feel comfortable around people '))
q12 = int(input('Insult people '))
q13 = int(input('Pay attention to details '))
q14 = int(input('Worry about things '))
q15 = int(input('Have a vivid imagination '))
q16 = int(input('Keep in the background '))
q17 = int(input('Sympathize with others\' feelings '))
q18 = int(input('Make a mess of things '))
q19 = int(input('Seldom feel blue '))
q20 = int(input('Am not interested in abstract ideas '))
q21 = int(input('Start conversations '))
q22 = int(input('Am not interested in other people\'s problems '))
q23 = int(input('Get chores done right away '))
q24 = int(input('Am easily disturbed '))
q25 = int(input('Have excellent ideas '))
q26 = int(input('Have little to say '))
q27 = int(input('Have a soft heart '))
q28 = int(input('Often forget to put things back in their proper place '))
q29 = int(input('Get upset easily '))
q30 = int(input('Do not have a good imagination '))
q31 = int(input('Talk to a lot of different people at parties '))
q32 = int(input('Am not really interested in others '))
q33 = int(input('Like order '))
q34 = int(input('Change my mood a lot '))
q35 = int(input('Am quick to understand things '))
q36 = int(input('Don\'t like to draw attention to myself '))
q37 = int(input('Take time out for others '))
q38 = int(input('Shirk my duties '))
q39 = int(input('Have frequent mood swings '))
q40 = int(input('Use difficult words '))
q41 = int(input('Don\'t mind being the center of attention '))
q42 = int(input('Feel others\' emotions '))
q43 = int(input('Follow a schedule '))
q44 = int(input('Get irritated easily '))
q45 = int(input('Spend time reflecting on things '))
q46 = int(input('Am quiet around strangers '))
q47 = int(input('Make people feel at ease '))
q48 = int(input('Am exacting in my work '))
q49 = int(input('Often feel blue '))
q50 = int(input('Am full of ideas '))

# calculate the final score for O, C, E, A, N
# convert the scores to z-scores
# print the 5 scores and z-scores

E = 20 + q1 - q6 + q11 - q16 + q21 - q26 + q31 - q36 + q41 - q46
A = 14 - q2 + q7 - q12 - q17 - q22 + q27 - q32 + q37 + q42 + q47
C = 14 + q3 - q8 - q13 - q18 + q23 - q28 + q33 - q38 + q43 + q48
N = 38 - q4 + q9 - q14 + q19 - q24 - q29 - q34 - q39 - q44 - q49
O = 8 + q5 - q10 + q15 - q20 + q25 - q30 + q35 + q40 + q45 + q50

with open('big5_summary.txt', 'r') as file:
    lines = file.readlines()[1:]
    name_map = {}
    for line in lines:
        name, mean, sd = line.split()
        name_map[name] = (float(mean), float(sd))


def z_score(name, raw):
    mean, sd = name_map.get(name, (0, 0))
    return (raw - mean) / sd


print('E: raw: %d, z: %.02f' % (E, z_score('extraversion', E)))
print('A: raw: %d, z: %.02f' % (A, z_score('agreeableness', A)))
print('C: raw: %d, z: %.02f' % (C, z_score('conscientiousness', C)))
print('N: raw: %d, z: %.02f' % (N, z_score('neuroticism', N)))
print('O: raw: %d, z: %.02f' % (O, z_score('openness', O)))
