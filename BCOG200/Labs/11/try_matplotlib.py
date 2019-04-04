"""
    Matplotlib is python's most popular graphing and data plot producing
    library. Matplotlib is not a part of core
    python. It is an add-on module, so you will have to follow the pip
    install procedure to install it. If you cant
    remmeber how, refer back to how we installed numpy and nltk.

    pyplot is a submodule of matplotlib, and it has many of the basic
    plotting functions we will use. One you have
    installed matplotlib, import matplotlib as below.

    I've commented out the commands that actually create the plots below.
    Uncomment them and the plots will appear.

"""
import matplotlib.pyplot as plt
import numpy as np

# first let's make up some data to plot.
days = np.arange(1, 6)
some_array1 = np.array([-1, -4.5, 16, 23, 30])
some_array2 = np.array([4, -3.5, -10, 25, 20])

# then plot the data
plt.plot(some_array1)
plt.show()

"""
It couldn't be simpler to plot a line of data. You just call plt.plot() and 
pass it the data.

When you are done, close the figure that it creates. We will keep creating 
more, and you dont want a billion open 
when you are done.

There are, of course, a billion options to make the plot look better, 
like adding figure captions, changing colors and shapes and all that stuff.
You'll have to consult the week's readings for all the color and style options
"""

# labels the 's-.r' affects the color and style of the lines. The readings
# give you all the options.
# the label="You" is what shows up in the legend if you have a legend.
plt.plot(days, some_array1, 's-.r', label="You")
plt.plot(days, some_array2, 's-.c', label="Me")

# Always, always, always label your axes!
plt.xlabel("Day")
plt.ylabel("Happiness")

# Set the minimum and maximum range of the axes
plt.xlim(0, 6)
plt.ylim(-20, 40)

# show the legend
plt.legend(loc='upper left')

# Conclude by making the plot appear in its own window. Until this step,
# a plot object exists, but hasnt been displayed.
plt.show()

# change this plot in various ways to make some other plot that looks different.

"""
    Ok, now let's plot some real data. Well, not real data. Fake, made up 
    data. But data that is more realistic.
    So we are going to imagine that we have IQ tests taken by 100 students at 
    3 universities, and GPAs for the same
    students. We will generate this data randomly. Well, kind of randomly; 
    based on my biases...
"""
# A list of schools
school_list = ['Illinois', 'Indiana', 'Northwestern']
# Type of data
score_type = ['IQ List', 'GPA']

# The matrix of IQ
iq_matrix = np.random.normal(100, 10, [1000, 3])
# The matrix of GPA
gpa_matrix = np.random.normal(3, 0.25, [1000, 3])
# Illinois is 10 IQ smarter
iq_matrix[:, 0] += 10
# Northwestern is 10 IQ dumper
iq_matrix[:, 2] -= 10
# Illinois has 0.25 higher GPA
gpa_matrix[:, 0] += 0.25
# Northwestern is 0.25 GPA lower
gpa_matrix[:, 2] -= 0.25
# GPA should not be outside of range [0, 4]
gpa_matrix = np.clip(gpa_matrix, 0.0, 4.0)
# Depth wise stack
data_matrix = np.dstack((iq_matrix, gpa_matrix))
# Print out the shape of the matrix
print(data_matrix.shape)
means = data_matrix.mean(axis=0)
stdevs = data_matrix.std(axis=0)

# comment the code above to show you understand it.
# next, add code to compute means and standard deviations of gpa and IQ for
# each school
# and store in a single matrix with three rows (one for each school) and two
# columns (one for each score type).

"""
Now let's plot a histogram.
The code below plots all three groups next to each other. It's kinda hard to 
read.
Change the code so that it only prints out 1 group.
Change the bins value and comment on what it does
"""
# A histogram with 10 bins
plt.hist(iq_matrix, bins=10)
# Title is IQ  Histogram
plt.title("IQ  Histogram")
# X axis label is IQ
plt.xlabel("IQ")
# Y axis label is Frequency
plt.ylabel("Frequency")
# Show the plot
plt.show()

"""
Now let's make a bar plot
"""

# this creates an array starting at 0 and going up to the num_groups -1.
# Print it out to see.
# we use this to figure out the x-axis values at which we will plot our group
# labels.
num_groups = 3
x_pos = np.arange(num_groups)

# create a bar chart, specifying the x-values at which our bars are
# positioned, then the y-values
# the next line wont work if you havent correctly computed mean and standard
# deviations and stored them in the
# matrices named 'means' and 'stdevs'
print('Shape:', means.shape)
plt.bar(x_pos, means[:, 0], align='center', yerr=stdevs[:, 0])
plt.xticks(x_pos, school_list)
plt.ylabel('IQ')
plt.ylim(50, 150)
plt.title('IQ by School')
plt.show()

"""
Now let's make a scatter plot
"""
# comment the code here and explain what is going on
# The color of the schools
colors = ("xkcd:navy", "xkcd:crimson", "xkcd:indigo")
# Iterate through school list
for i in range(len(school_list)):
    # Print out the number of rows in iq matrix and gpa matrix
    print(len(iq_matrix), len(gpa_matrix))
    # The plot with a scatter plot
    plt.scatter(iq_matrix[:, i], gpa_matrix[:, i],
                c=colors[i], edgecolors='none', s=30, label=school_list[i])
# Has title GPA and IQ by School
plt.title('GPA and IQ by School')
# Generate legend
plt.legend(loc=2)
# Show the graph
plt.show()
