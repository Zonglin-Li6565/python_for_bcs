"""
As I said, there are two things to keep track of when doing regex's in python.
The first is that there are different regex functions:
    1. findall()
    2. search()
    3. split()
    4. sub()

The second thing, and the thing that makes regex really powerful, is that you
can use all sorts of special
'meta-characters' that modify how the search is performed. These include:
"""

"""
For example, using a period in a re search treats the period as a "wild 
card". Note how the search below matches
both the word spring and the word seeing, because they both meet the search 
criteria.
"""
import re

some_text = "It is spring. I like the spring-time! I am hoping for a " \
            "superspring. I look forward to seeing the spring!"
x = re.findall('s..ing', some_text)
print(x)

"""
Other meta-characters allow you to search to see if a string starts with or 
ends with a particular sequence. Think of
these as just a normal find-all search, where you've placed limits on what 
counts as a match (that it must be at the
beginning if preceded by a ^, and at the end if ending with a $.
"""
some_text = "Seasons: Fall, spring, summer, winter"
a = re.findall('^Seasons', some_text)
b = re.findall('^Seasons:', some_text)
c = re.findall('winter$', some_text)
d = re.findall('summer$', some_text)
print(a)
print(b)
print(c)
print(d)

"""
What happens if you actually want to search for a dollar sign or other 
special characters? You can use a \ to "escape"
the special character, or to treat it as a regular string.
"""
some_text = "$5 is all I will give you."
a = re.findall('$5', some_text)
b = re.findall('\$5', some_text)
print(a)
print(b)

"""
You can search for more complicated stuff, like if one thing follows another 
thing by using a +, which means, 
search for the :
"""

some_text = "I was surprised to find that I liked Taylor Swiftt. But I still " \
            "prefer Taylor Dayne."
a = re.findall('Taylor Swift+', some_text)
b = re.findall('Taylor_Swift+', some_text)
c = re.findall('TaylorSwift+', some_text)
print(a)
print(b)
print(c)

"""
Now, you might be wondering, what's the differencing between searching for a 
"Taylor" followed by a "Swift", and just
searching for "Taylor Swift" directly? Check out below:
"""
some_text = "I like Taylor Swif. But I still prefer Taylor Dayne. It's " \
            "Taylor 'Hey Look!' Swift"
a = re.findall('Taylor Swift*', some_text)
b = re.findall('Taylor Swift', some_text)
print(a)
print(b)

"""
The two behave the same. They notice the first Taylor Swift, but miss the 
second one where there is something in between.
What if we want to count the second one as well? We can combine some of what 
we've learned to do some really powerful
searches This search is basically specifying I want a record of all 
occurrences of Taylor that are followed by one
or more occurrences of Swift, even if there is one characters (of any time) 
in between them.
"""
some_text = r"I like Taylor Swift. But I still prefer Taylor Dayne. It's " \
            r"Taylor 'Hey Look!' Swift"
a = re.findall('Taylor.+Swift+', some_text)
print(a)
# play around with some other complicated search expressions. Make three of
# your own text strings, and then construct
# at least five searches on them to play around with finding matches of
# various types.

some_text = 'This is a valid email address: helloworld@illinois.edu'
a = re.findall(r'(\w+@\w+\.\w+)', some_text)
print(a)
some_text = '<https://api.github.com/user/11804383/received_events?page=2>; ' \
            'rel="next", ' \
            '<https://api.github.com/user/11804383/received_events?page=8>; ' \
            'rel="last"'

next_link = re.findall(r'( |^)(<.*>); rel="next"', some_text)
print(next_link)
last_link = re.findall(r'( |^)(<http.*>); rel="last"', some_text)
print(last_link)
next_page_num = re.findall(r'( |^)<.*page=([0-9]+)>; rel="next"', some_text)
print(next_page_num)
last_page_num = re.findall(r'( |^)<http.*page=([0-9]+)>; rel="last"', some_text)
print(last_page_num)

"""
A final interesting situation is that you can search for sets of characters.
# for each findall below, add a comment line explaining what is happening.
# Experiment with different stuff in the brackets to see what works and what 
does not.
"""
some_text = "The rain will be here again. You know what they say about April! " \
            "" \
            "" \
            "" \
            "" \
            "I think there are 31 days in April."
# Find all a, r, n characters
print(re.findall("[arn]", some_text))
# Find all characters that are not either a, r, or n
print(re.findall("[^arn]", some_text))
# Find all characters in between a and n inclusively
print(re.findall("[a-n]", some_text))
# Find all 0, 1, 2, 3 characters
print(re.findall("[0123]", some_text))
# Find all 0, 1, 2 characters
print(re.findall("[0-2]", some_text))
# Find all 31s
print(re.findall("[3][1]", some_text))
