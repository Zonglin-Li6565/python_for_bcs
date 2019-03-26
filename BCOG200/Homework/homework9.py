def q1():
    print("Question 1:"
          "Explain the behavior of Vehicle 1. "
          "What is an example of a way that Braitenberg says that vehicle one "
          "could behave in a way that makes "
          "it look more complex than it really is? "
          "Can you think of other examples?")
    #
    your_answer = """
    Vehicle 1 will speed up when it's close to the heat source, and slow down 
    when it's getting farther away. The speed to inverse proportional to the 
    distance to a heat source.
    
    In the book Braitenberg says the vehicle seems alive, since it doesn't 
    like warm water. And it couldn't turn back. Other example could be the 
    transition between potential energy and kinetic energy. When the vehicle 
    is far from the source, it has high potential energy, and low kinetic 
    energy. When it's close to the source, it has high kinetic energy and low 
    potential energy.
    """
    print(your_answer)


def q2():
    print("Question 2: "
          "The varieties of Vehicle 2 behave in ways that Braitenberg says "
          "remind of us of a more complex "
          "organism demonstrating fear and aggression. Explain why this is so? "
          "Think of another example of human behavior where something complex "
          "is in fact possibly explainable "
          "by something much simpler, and give an example of the "
          "hypothetically simpler explanation.")
    #
    your_answer = """
    The way the sensors are connected to the motors make the difference. If 
    the connection is direct (i.e. no cross) the vehicle will move away from 
    the heat source, since the motor close to the heat source will spin 
    faster, and therefore turn the vehicle away. However, if the connection 
    is crossed, the vehicle will turn towards heat source since the motor on 
    the other side spins faster. The cross connection will eventually go 
    through the heat source at high velocity which is similar to aggression.
    
    Another example of potentially explainable human behavior is gathering. 
    We can explain it with a modified vehicle1. Instead of making 
    velocity inversely proportional to the distance, we can make it 
    proportional. In that way the vehicles will eventually all stop near the 
    heat source.
    """
    print(your_answer)


def q3():
    print("Question 3: "
          "Vehicle 3 discusses the nature of knowledge. What does Braitenberg "
          "say about what knowledge is in this "
          "chapter? Do you agree with Braitenberg? Why or why not?")
    #
    your_answer = """
    He said knowledge is a flow of information from the environment into a 
    living being or at least something like a living being. I agree wih 
    Braitenberg, but also believe there's more. In my opinion, knowledge 
    should also emphasis on the retaining of information inside the creature.
    """
    print(your_answer)


def q4():
    print("""Question 4:
          Complete Vehicle3.py as described in Lab. Make sure you have 
          implemented the following:
            - Add at least 1 more class representing another kind of input 
            other than heat.
            - Have the input_list contain multiple kinds of input sources.
            - Use custom images for each input sources
            - Modify vehicle 3 so that it has an 'innate preference' or 
            'innate dislike' of each kind of input""")

    your_answer = """
    See Vehicle3.py
    """
    print(your_answer)


def q5():
    print("""Question 5:
    Create Vehicle4.py by saving a copy of your Vehicle3.py file and saving 
    it as Vehicle4.py.
    Modify the vehicle so that, for things that it likes, it has a 'u-shaped' 
    preference curve, moving little
    when it is far away from something, or when it is really close, 
    but moving quickly when it is a moderate distance
    away. If you get this working correctly, you should get your Vehicles 
    approaching and staying near the things they
    like.
    """)
    #
    your_answer = """
    See Vehicle4.py
    """
    print(your_answer)


def main():
    q1()
    q2()
    q3()
    q4()
    q5()


main()
