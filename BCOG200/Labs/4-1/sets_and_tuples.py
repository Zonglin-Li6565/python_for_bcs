# remember that a "tuple" is like a list, except that it is "immutable", meaning it cannot be changed once it is
#   created.
my_tuple = ("lion", "tiger", "bear")

# try doing all the stuff with lists that you might want to do, like accessing an item by element,
# adding an element, removing an element. See what happens and report your results.

# why would you want this?
#   1) the code runs faster
#   2) it is a way to protect yourself from accidently changing something you know you dont want to change

# sets are like lists, except that you cant have duplicates.
my_set = set()

# you can add items easily
my_set.add('lion')
my_set.add('tiger')
my_set.add('bear')
# add some more animals to your set. make sure you try to add a duplicate and see what happens
my_set.add('lion')
assert len(my_set) == 3
my_set.add('human')
assert len(my_set) == 4

# hear are some other functions you can do with a set. test them and see what they do, and explain in the comments
my_set.discard('lion')  # Removes an element from the set if it's present
my_set.remove('human')  # Removes an element from the set. Must be the memeber
# Make a copy of set. Only copy the reference
# to the object, not the object itself.
my_set.copy()
# Removes all the element from this set
my_set.clear()
# Return the union of this set and an iterable
my_set.union()
# Return the intersection of this set and an iterable
my_set.intersection()
# Return a new set containing all the elements in this set but not in the other
# set or iterable
my_set.difference()
# Removes all the elements of the other set from this set
my_set.difference_update()
# Checks whether the two sets have no common element
my_set.isdisjoint()
# Check whether this set is a subset of another set
my_set.issubset()
# Check whether this set contains another set
my_set.issuperset()

# explain what happens here:
# Returns a set containing all the unique characters of the string
my_set = set("abcdefghijklmnopqrstuvwxyz")
# Returns a set containing three string 'a', 'b', and 'c'
my_set = set(['a', 'b', 'c'])
