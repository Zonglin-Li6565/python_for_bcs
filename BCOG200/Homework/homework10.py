def q1():
    print("Question 1 (10 Points)")
    # According to the readings for this week, what is the field of natural
    # language processing, and what are some
    # of it's primary goals or problems that it is used to solve?
    your_answer = """
    According to Wikipedia: Natural language processing (NLP) is a subfield 
    of computer science, information engineering, and artificial intelligence 
    concerned with the interactions between computers and human (natural) 
    languages, in particular how to program computers to process and analyze 
    large amounts of natural language data.
    """
    print(your_answer)


def q2():
    print("Question 2 (10 Points)")
    # Describe a psychological question or issue that involves language that
    # you find interesting, and describe how
    # you might use natural language processing techniques to solve it.
    your_answer = """Sentiment analysis. Finding the emotion conveyed through 
    language. We can train a model to classify text into different sentiments 
    based on features such as word frequency and others. 
    """
    print(your_answer)


def q3():
    print("Question 3 (10 Points)")
    # According to the readings for this week, what are the some of the
    # differences between rule-based and
    # statistical natural language processing?
    your_answer = """In rule based NLP, the programmer has to know the rules 
    and hard code it into the program. But in statistical NLP, you let the 
    computer to find the rules automatically.
    """
    print(your_answer)


def q4():
    print("Question 4 (10 Points)")
    # List three differences between re.search() and re.findall()
    your_answer = """re.search returns the first matched instance, 
    and re.findall returns all the matches"""
    print(your_answer)


def q5():
    print("Question 5 (10 Points)")
    # Explain this code
    # import re
    # fh = open("simpsons_phone_book.txt")
    # for line in fh:
    #     if re.search(r"J.*Neu", line):
    #         print(line.rstrip())
    # fh.close()
    your_answer = """First we open the file of `simpsons_phone_book.txt`. 
    Then for each line, we search whether there's a substring that starts 
    with J and ends with Neu, if so, we print whole line without the ending 
    spaces."""
    print(your_answer)


def q6():
    print("Question 6 (10 Points)")
    # What is a "stop word", and how can you use NLTK to remove stop words
    # from an NLTK text document?
    your_answer = """Stop word: the common words that are usually filtered out.
    To remove stop words:
    ```
    from nltk.corpus import stopwords
    removed = list(filter(lambda w: not w in stopwords.words('english'), words))
    ```
    """
    print(your_answer)


def q7():
    print("Question 7 (40 Points)")
    # Write a program that
    #   - Imports five books of your choice from project gutenberg, using the
    #   code from try_nltk.py
    #   - Tokenizes and lower-cases all the words in the book
    #   - Creates a text object from each book
    #   - Removes stop words from each text object
    #   - Uses NLTK's part of speech tagger to get each word's part of speech
    #   - Uses NLTK's FreqDist() to get word frequency distributions
    #   - Prints out the 10 most frequent nouns, verbs, and adjectives in
    #   each book, looking like this:
    #
    #   MOBY DICK
    #   Nouns: whale, boat, ocean, ...
    #   Verbs: chase, fish, sail, ...
    #   Adjectives: white, wet, big, ...
    #
    #   ALICE IN WONDERLAND
    #   Nouns: rabbit, boat, ocean, ...
    #   Verbs: drink, eat, sail, ...
    #   Adjectives: white, wet, big, ...
    your_answer = "See hw10q7.py"
    print(your_answer)


def main():
    q1()
    q2()
    q3()
    q4()
    q5()
    q6()
    q7()


main()
