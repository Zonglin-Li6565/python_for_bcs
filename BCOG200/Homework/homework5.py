def q1():
    # What is the difference between an argument and a parameter? Given an example.
    your_answer = """
    A parameter is the variable name in the function signature. An argument is 
    the data passed into the function.
    """
    print("Question 1")
    print(your_answer)


def q2():
    # The function below is called a 'nonfruitful' because it doesnt return a value. But it actually does return a
    # value, silently. How can you see what that value is? What is it? What is an exmaple of a function we have used
    # that is a nonfruitful function?

    def nonfruitful_function():
        print("all this function does is print me out")

    print("Question 2")
    nonfruitful_function()
    your_answer = """
    The return value is None. To see it you can call the function and pass the 
    returned value to a print function:
    print(nonfruitful_function())
    This function (q2) is an example of nonfruitful function.
    """
    print(your_answer)


def q3():
    # what is wrong with the code below?
    #
    # def function1():
    #     print("This is function 1")
    #
    #     def function2():
    #         print("This is function 2")
    #
    # function1()
    # function2()

    your_answer = """
    function2 is a closure inside function1, which is not accessible in the 
    scope of q3.
    """
    print("Question 3")
    print(your_answer)


def q4():
    # below this function definition, there is a global variable defined. What about python's syntax makes it a
    # global variable? How would you make it a local variable to this function?

    your_answer = """
    The variable doesn't have any indentation before it. So it's in the global
    scope. If we want to make it a local variable of this function, we should
    add four spaces before 'x = 25'
    """
    print("Question 4")
    print(your_answer)


x = 25


def q5():
    # What is an optional parameter in a python function, and how do you define one in a function definition?
    your_answer = """
    The optional parameter will have a keyword and a default value. The function
    returned from this function is an example.
    """
    print("Question 5")
    print(your_answer)

    def with_optional_args(positional1, positional2, optional1=1, optional2=2):
        print(positional1, positional2, optional1, optional2)

    return with_optional_args


def q6():
    # What is the function below doing? The function definition returns two values, but when the function is called
    # there is only one variable to which the data is being assigned? Why is this legal? How is handling this situation?
    def get_min_max(some_list):
        min = some_list[0]
        max = some_list[1]
        for value in some_list[1:]:
            if value > max:
                max = value
            if value < min:
                min = value
        return min, max

    print("Question 6")
    your_answer = """
    The function will find the largest and smallest number in a list. The 
    return statement `return min, max` essentially returns a tuple of min and 
    max, which is equivalent to `return (min, max)` 
    """
    my_list = [-6, 2, 5, 5, -1, 3]
    min_max = get_min_max(my_list)
    print(min_max)
    print(your_answer)


def q7():
    # Explain how sys.argv works. What kind of data structure is created, and what information is put in that data
    # structure?

    your_answer = """
    For a command like:
    `python lyrics.py lyrics_dir`
    bash will parse it into executable ('python') and arguments 
    (lyrics.py, lyrics_dir). Then python interpreter will create a list and 
    assign it to a variable under sys called argv.
    """
    print("Question 7")
    print(your_answer)


def q8():
    # Define a function that can take a variable number of input arguments, and if all the arguments are numbers,
    # calculates and returns the variance of those numbers. print

    def var_args_variance(*args):
        for arg in args:
            if not isinstance(arg, (int, float, complex)):
                return 0
        mean = sum(args) / len(args)
        mean_of_square = sum(map(lambda n: n ** 2, args)) / len(args)
        return mean_of_square - mean ** 2

    print("Question 8")
    nums = [1, 2, 3, 4, 5]
    print('numbers:', nums)
    print('variance:', var_args_variance(*nums))


def q9():
    # What is the problem with the code below that defines and calls a function? Type your answer where it says
    # 'your_answer. Then, uncomment and fix the code so that it does not generate an error, prints out "yes" if the
    # input argument is "dog", prints out no otherwise, and returns either "yes" or "no" when the function is complete.

    def dog_identifier(x):
        if x == "dog":
            print("yes")
        else:
            print("no")

    input_string = input("Type Something: ")
    dog_identifier(input_string)

    your_answer = """
    The syntax is invalid. It's missing the parameter. And it didn't return 
    anything
    """
    print("Question 9")
    print(your_answer)


def q10():
    # write a function that takes a list as an input, and calculates mean, median, and mode of those numbers,
    # and returns them.

    # your function definition here
    def computes_a_lot_of_things(num_list):
        if len(num_list) == 0:
            return 0, 0, 0
        sorted_list = sorted(num_list)
        mean = sum(sorted_list) / len(sorted_list)
        median_idx = len(sorted_list) // 2
        median = sorted_list[median_idx]
        if len(sorted_list) % 2 == 0:
            median = (median + sorted_list[median_idx + 1]) / 2
        num_counter = {}
        for num in sorted_list:
            if num not in num_counter:
                num_counter[num] = 0
            num_counter[num] += 1
        sorted_by_occurrence = sorted(num_counter.items(), key=lambda x: x[1],
                                      reverse=True)
        mode = sorted_by_occurrence[0][0]
        return mean, median, mode

    data = [6, 7, 8, 9, 9, 9, 9, 10, 11, 12]
    # call the function here
    mean, median, mode = computes_a_lot_of_things(data)
    print("Question 10")
    print(mean, median, mode)


def main():
    # call all of the question functions (q1 through q10) in the main function so that they all run and execute
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()
    q9()
    q10()


if __name__ == '__main__':
    main()
