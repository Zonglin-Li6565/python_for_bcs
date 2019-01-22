number_list = []

object_list = ['dog', 'cat', 'shoe', 'sock']

# print(number_list)
# print(object_list)
#
# print(object_list[1])
#
# print(number_list[1])
#
# number_list.append(5)
# number_list.append(6)
# print(number_list)
#
# object_list.append('car')
# print(object_list)
#
# if 'shirt' in object_list:
#     print('shirt is in the list')
# else:
#     print('no shirt in the list')
#
# object_list[3] = 'shirt'
# print(object_list)
#
# if 'shirt' in object_list:
#     print('shirt is in the list')
# else:
#     print('no shirt in the list')
#
# num_items = len(object_list)
# print("there are {} items in object list".format(num_items))

# Questions:
#
# 1. if i wanted to insert 'tree' into the 3rd position in the object list,
#    so that it does NOT replace any items,
#    how do I do that?
object_list.insert(2, 'tree')
print(object_list)
# 2. what is the difference between list.pop() and list.remove()
# >> list.pop() will remove the specified object at index, and returns the
#    object
# >> list.remove() will match the object in the list and remove it
# 3. print out the object list, sorted in reverse alphabetical order
print(list(reversed(sorted(object_list))))

