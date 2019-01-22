x = 2
y = 0

for i in range(10):
    y += x ** 2
    print(i, x, y)

food_list = ['pizza', 'sandwich', 'apple', 'ice cream', 'salad']
score_list = [1, 3, 4, 5, 2]

# what will the following code do

for food in food_list:
    print(food)
# >> Print out the food name in each line

# what will the following code do
num_foods = len(food_list)
for i in range(num_foods):
    print(food_list[i], score_list[i])
# >> Print out the food name and the score on the same line for each food

# what will the following code do
combined_list = []
for i in range(num_foods):
    new_pair = [score_list[i], food_list[i]]
    combined_list.append(new_pair)
    combined_list.sort()
print(combined_list)
# >> Print out the food sorted from low score to high score

# what will the following code do
for word in food_list:
    for letter in word:
        print(letter)
    print()
# >> Print out the characters of the food name in a separate line and a new
#    line between each food
