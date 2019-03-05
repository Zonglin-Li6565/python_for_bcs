def q1():
    print("\nQuestion 1 is worth 1 point.")
    # What is the difference between a function and a method in python?

    your_answer = """
    A function is independent from any class. A method is an operation on a 
    class's attributes.
    """
    print(your_answer)


def q2():
    print("\nQuestion 2 is worth 1 point.")
    # What is the difference between a class and a class instance in python?

    your_answer = """
    A class is a blueprint of a type of objects. A class instance is a bundle of
    data and operations that are constructed according to the blueprint.
    """
    print(your_answer)


def q3():
    print("\nQuestion 3 is worth 1 point.")

    # In most cases, python is an object-oriented language. What does this
    # mean? Give an example of a way in which
    # python is object oriented. Give an example of a situation where python
    # is not object oriented, and behaves more
    # like a functional programming language.

    your_answer = """
    Why it's object-oriented: Everything in python is an object, even 
    class definitions. So in that sense python is object oriented. One example
    is that type(type) will return class 'type'.
    However, since function is also an object, python treats it as first class
    object. Therefore we can also apply functional techniques in python. 
    Examples are: higher order functions like map or reduce, function closures.
    """
    print(your_answer)


def q4():
    print("Question 4 is worth 1 point.")
    # Explain what 'self' means for python classes. What are the different
    # situations where we typically need to use 'self'?

    your_answer = """
    By default the first parameter of a method is self, which is a reference to
    the current object. We need to use self when the method needs access to
    class attributes or other methods.
    """
    print(your_answer)


def q5():
    print("Question 5 is worth 1 point.")

    # What is wrong with the following code? Explain what is happening in as
    # much detail as you can.

    class human:
        pass

    jon = human.extroversion = 10
    try:
        print(jon.extroversion)
    except Exception as e:
        print("This code doesn't work")
        print(e)

    answer = """
    First we created a class called human. Then we create a static variable
    named extroversion in class human and make it refer to 10. We then
    assign the same reference to a variable called jon. So jon and
    extroversion in human have the same reference (checked using id) to 10. When
    we are trying to access the extroversion attribute of jon, it will raise
    an AttributeError saying that int doesn't have attribute extroversion 
    """
    print(answer)


def q6():
    print("Question 6 is worth 1 point.")

    # How do you access a class's attributes using it's attribute dictionary?
    # Write code below that prints out all the attributes of the class.

    class automobile:
        def __init__(self, make, model, year):
            make = None
            model = None
            year = None

    my_car = automobile('honda', 'civic', '2013')
    for key, val in my_car.__dict__:
        print(key, val)


def q7():
    print("Question 7 is worth 2 points.")
    # Create a separate python script called humans.py. Add a main function,
    # and our definition of the human class from
    # this week's lab. Implement the following additions to that program:
    #   1) Add a function to the human called "ask_question", that prints out
    #      a random question from a list of questions that you have hard-coded
    #      into the class.
    #   2) Add a function called "answer_question" that randomly print 'yes'
    #      or 'no', to a question that the function
    #      takes as an input parameter.
    #   3) in the main function, create two instances of the human class
    #   4) create a loop that cycles 10 times, each time through the loop the
    #      program should:
    #      - pause for 10 seconds (consult the documentation for the time
    #      module on how to do this...
    #      - randomly choose one of the humans to ask a question
    #      - have the other agent answer the question using it's
    #      answer_question function

    print('See human.py')


def q8():
    print("Question 8 is worth 2 points.")

    # Complete the code for the this week's lab. Normally the lab is
    # participation. This week it is the homework
    # as well, and must be completed and working correctly.

    print('See Labs/7')


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()
    q8()


main()
