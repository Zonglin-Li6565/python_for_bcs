'''
    there are many libraries we might want that are not a part of the
    standard library.
    Two of them are numpy (for matrix algebra and all around faster math and
    data processing.
    To use libraries that are not a part of the standard library, first you
    need to get
    them. At the command window, type:
        python -m pip install numpy

    NOTE: Make sure that you type the lines above like you are running a
    normal python program. So if you normally type
    python3, then type: python3 -m pip install numpy.

    This should install these libraries for you. You might already have them
    (some installations of python do come
    with these because they are so popular. If so, you'll get a message
    saying "Requirement already satisfied".
'''
#

'''
    numpy does basic, high performance number crunching, especially for data 
    in vector or matrix form. In numpy
    we call these data structures arrays.
    
    as always, first we have to import the library we want to use. You may 
    note that the import statement is a little 
    different here. that "as np" part of it is just letting us refer to numpy 
    using the shorter np instead of having to 
    type out numpy every time. We can do this anytime we import a library, 
    giving it a special name will have in our 
    program. Usually this only happens with long library names that we want 
    to shorten.
'''
import numpy as np

# next we create some arrays. Numpy arrays are a lot like lists, except that
# they have to be numbers.
# note here we are actually passing a list to np as an input argument to it's
# array function, and getting an array back.
print("Basic Array Creation")
my_1D_list = [1, 2, 3]
my_1D_matrix = np.array(my_1D_list)

# what's different when you look at lists versus np arrays?
# list is of List type which is built in to python. numpy array is of type
# np.array which uses a different data structure to store the numbers and
# offers much more operations.
print(my_1D_list)
print(my_1D_matrix)

# multidimensional arrays have different syntax from lists of lists. In a lot
# of ways the np way is more intuitive.
my_2D_list = [[1, 2, 3], [4, 5, 6]]
my_2D_matrix = np.array(my_2D_list)
print(my_2D_list)
print(my_2D_matrix)
# create a 3D list (a list of lists of lists) and then convert it to a 3-D
# array and print it out

my_3D_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
my_3d_matrix = np.array(my_3D_list)

# we can see the size of our arrays really easily. This is like doing len().
print(my_2D_matrix.shape)
print("")

# numpy gives us many ways to create arrays. Comment them below. Note also
# where you can use float/int
# as an input argument, and what it does.
print("Advanced Array Creation")
# Create a numpy array of shape (2, 4) of type float, containing zeros.
a = np.zeros((2, 4), float)
# Create a numpy array of shape (2, 4) of type int, containing ones.
b = np.ones((2, 4), int)
# Create a numpy array of shape (4, 2) filled with 7 in type float.
c = np.full((4, 2), 7, float)
# Create an identity matrix of shape (4, 4)
d = np.eye(4)
# Create a random matrix in range [0, 1) of shape (2, 4)
e = np.random.random((2, 4))
print("Here are some different arrays")
print("zeros\n", a)
print("ones\n", b)
print("full\n", c)
print("eye\n", d)
print("random\n", e)
print("")

# we access members of an array in a way similar to lists:
print("Array Indexing")
# Create a random array of size 10 with numbers in range [1, 10)
e = np.random.randint(1, 10, (10))
print(e)
print("The 1D array, item by item")
for i in range(len(e)):
    print(e[i])
print("")

# if the array is more than 1-D, the syntax is slightly different than for
# lists. In comments, what is the difference?
# Now it's a 2D array of shape (2, 4)
e = np.random.randint(1, 10, (2, 4))
print(e)
print("The 2D array, item by item")
for i in range(e.shape[0]):
    for j in range(e.shape[1]):
        print(e[i, j])
print("")

# you can use 'slicing' to pull out subsets of arrays. What do the following
# slices do, and why?
print("Array slicing")
e = np.random.randint(1, 10, (10, 20))
print(e)
# Take the second column
c2 = e[:, 1]
# Take the first row
r1 = e[0, :]
# Take the elements on row 2, 3 and on column 2, 3, 4
f = e[1:3, 1:4]
print(r1)
print(c2)
print(f)
print("")

# you can do all sorts of funky math on np arrays. Uncomment the code and run
# it, line by line.
# add comments that explain what's happening.
# some of the lines generate errors. Leave those lines commented out,
# but explain why it generates an error.
print("Array Math")
# Create a random matrix of shape (4, 5)
x = np.random.randint(1, 5, (4, 5))
# Create an identity matrix of size (5, 5)
y = np.eye(5).astype(int)
# Create a matrix of size (4, 5) filled with 1 and has type int
z = np.ones((4, 5), int)
print("x\n", x)
print("y\n", y)
print("z\n", z)

print("Array element arithmetic")
# Set an element at forth row and forth column in y to 4
y[3, 3] = 4
# Increment element at 1, 3 in z by one
z[1, 3] += 1
# Assign element at 1, 4 in z to the product of x[0, 0] and y[3, 3]
z[1, 4] = x[0, 0] * y[3, 3]
print("x\n", x)
print("y\n", y)
print("z\n", z)

print("Array arithmetic")
# Element wise addition of x and z
a = x + z
# Shape incompatible
# b = y + z
# Divide all elements in x by 5.0 and assign it to c
c = x / 5.0
# Increase element at 1, 3 in z by one.
z[1, 3] += 1
# Make element at 1, 4 be the product of (0, 0) in x and (3, 3) in y
z[1, 4] = x[0, 0] * y[3, 3]
print("x\n", x)
print("y\n", y)
print("z\n", z)
print("a\n", a)
print("c\n", c)
print("")

print("Matrix algebra")
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 5, 10, 5, 10])
# Element wise multiplication between a and b
c = a * b
# Computes dot product between a and b (one is treated as column vector and
# the other is row vector)
d = np.dot(a, b)
print("a\n", a)
print("b\n", b)
print("c\n", c)
print("d\n", d)
x = np.random.randint(1, 10, (3, 4))
y = np.random.randint(1, 10, (3, 4))
print("x\n", x)
print("y\n", y)
# Type incompatiable. you need to transpose x or y first.
# z = np.dot(x,y)
# Element multiplication
z = x * y
print("z\n", z)
print("")

print("Matrix Summarization")
y = np.random.randint(1, 10, (3, 4))
# Add all the elements in y up.
sum1 = y.sum()
# Add each column in y up
sum2 = y.sum(0)
# Add each row in y up
sum3 = y.sum(1)
# y only has two dimensions
# s4 = y.sum(2)
print("y\n", y)
print("sum1:", sum1)
print("sum2:", sum2)
print("sum3:", sum3)

# Mean of all elements in y
mean1 = y.mean()
# Mean of each columns in y
mean2 = y.mean(0)
# Mean of each row in y
mean3 = y.mean(1)
print("mean1:", mean1)
print("mean2:", mean2)
print("mean3:", mean3)

# Sd of all elements in y
stdev1 = y.std()
# Sd of each column in y
stdev2 = y.std(0)
# Sd of each row in y
stdev3 = y.std(1)
print("stdev1:", stdev1)
print("stdev2:", stdev2)
print("stdev3:", stdev3)
