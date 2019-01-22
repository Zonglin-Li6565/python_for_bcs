X = 'dog'
Y = 'pizza'
Z = 'shoe'

A = '5'
B = 30
C = 4.0

# 1. what is the output of the following statements
#     print(A+B)
#     >> TypeError
#     print(B+C)
#     >> 34.0
#     print(X+Z)
#     >> 'dogshoe'
#     print(Y+A)
#     >> 'pizza5'
#     print(Z+B)
#     >> TypeError
#
# 2. what do the following statements do:
#     B += 5
#     >> B = 35
#     D = C ** 2
#     >> D = 16.0
#     D = B / C
#     >> D = 7.5
#     D = B // C
#     >> D = 4.0
#     D = B % C
#     >> D = 2.0
#
# 3. What is the difference between the following two statements?
#     B = 20
#     >> Assignment expr
#     B == 20
#     >> Bool expr. true if B is 20, false if not.
#
# 4. if you wanted to print out X and B, resulting in "DOG 30", how would you do that?
#    >> print('%s %d' % (X, B))
