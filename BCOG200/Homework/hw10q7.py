import os

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

directory = 'books'

interesting_books = ['ALICE_IN_WONDERLAND.txt', 'FRANKENSTEIN.txt',
                     'GRIMMS_FAIRY_TALES.txt', 'HUCK_FINN.txt', 'MOBY_DICK.txt']

for book in interesting_books:
    with open(os.path.join(directory, book), 'r') as file:
        content = file.read().lower()
        tokenizer = RegexpTokenizer(r'\w+')
        token = tokenizer.tokenize(content)
        no_stop = list(
            filter(lambda w: w not in stopwords.words('english'), token))
        text = nltk.Text(no_stop)
        tagged = nltk.pos_tag(no_stop)
        tag_dict = {}
        for word, tag in tagged:
            if tag not in tag_dict:
                tag_dict[tag] = []
            tag_dict[tag].append(word)

        print(book[:-4])
        for tag, words in tag_dict.items():
            fdist = nltk.FreqDist(words)
            print('%s:' % tag, end='')
            for word, _ in fdist.most_common(10):
                print(' %s' % word, end='')
            print()
        print()
