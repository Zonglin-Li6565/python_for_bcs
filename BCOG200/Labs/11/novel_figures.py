"""
This lab assignment is also the homework assignment for the week.

1) create a main function.
2) in the main function, create a variable called "novel_url_list", 
that contains a list of website urls from project
    gutenberg, for at least three novels of your choice. In addition, in the 
    main function create the following empty
    lists: 1) novel_tokens_list, 2) novel_fdist_list.
3) create a function called "get_novel()" that takes a single novel URL as an 
input, and uses the code from
    try_nltk.py to download and import the text from that novel. This 
    function should return two variables: 1) the
    novel's text as a lower-cased NLTK token_list, 2) an NLTK fdist object 
    for the novel
4) in the main function, create a for loop that iterates through every URL in 
the novel_url_list. In the for loop,
    call the "get_novel()" function, and add the resulting token lists and 
    fdists to novel_tokens_list and
    novel_fdist_list.
5) create a function called "plot_freq_dists()" that takes novel_fdist_list 
as an input. this function should create
    a matplotlib figure with a line plot. The line plot should have a 
    separate line for each novel, plotting the novel's
    frequency distribution. In other words, each line's x-value should be a 
    word's rank order (in terms of frequency),
    and each line's y-value should be a word's actual frequency. Make sure 
    that the figure has a title, that the axes
    are labeled, and that there is a legend specifying which novel is which 
    line. call this function from your main
    function.
6) create a function called "plot_most_freq_word()", that takes the 
novel_fdist_list as an input. this function should
    create a maplotlib multiple plot figure that has 1 column and n rows, 
    where n is the number of novels in fdist_list.
    each plot should be a bar plot that plots frequency of the ten most 
    frequent words. make sure this plot has a main
    title, a separate title for each plot specifying which novel it is, 
    and that the axes are labeled.  call this
    function from your main function.
7) add a second argument to the plot_most_freq_word() function specifying 
whether stop words should be removed, set to
    either True or False. If set to True, each fdist should have the stop 
    words removed before creating the bar plot.
    Make sure the title reflects whether this figure is using all words, 
    or only non-stop-words.
8) add a third argument to the plot_most_freq_word() function, that allows 
you to specify a part of speech, If this
    argument is set to None, plot the most frequent words using all parts of 
    speech. If a specific part of speech is
    specified, (like NN), then only include words from that part of speech in 
    the bar chart. Make sure the title
    reflects whether the figure includes all words, or only words from one 
    category.
9) make sure that plt.show() is not called until the very end, so that all
plots appear at the same time.
"""
from urllib import request

import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords


def plot_freq_dists(novel_fdist_list):
    freq_list = []
    min_length = 1e10
    for novel, _ in novel_fdist_list:
        freq = list(map(lambda x: x[1], novel.items()))
        freq.sort(reverse=True)
        freq_list.append(freq)
        min_length = min(len(freq), min_length)

    x_vals = list(range(min_length))

    for i, freq in enumerate(freq_list):
        plt.plot(x_vals, freq[:min_length], label=novel_fdist_list[i][1])

    plt.title('Word frequency of each book')
    plt.grid(True)
    plt.legend()
    plt.xlabel('Words rank order')
    plt.ylabel('Words real frequency')


def plot_most_freq_word(novel_fdist_list, remove_stop_word=False,
                        part_of_speech=None):
    fig, ax = plt.subplots(len(novel_fdist_list), 1, figsize=(12, 12))
    fig.tight_layout()
    fig.suptitle('Most frequent words of each book %s stop words %s' % (
        'without' if remove_stop_word else 'with',
        'only from %s' % part_of_speech if part_of_speech else 'for all words'))
    for i, novel_and_name in enumerate(novel_fdist_list):
        novel, book = novel_and_name

        items = novel.items()

        if remove_stop_word:
            items = filter(lambda x: x[0] not in stopwords.words('english'),
                           items)

        if part_of_speech:
            items = filter(
                # Bye bye performance
                lambda freq: nltk.pos_tag([freq[0]])[0][1] == part_of_speech,
                items)

        sorted_words = sorted(items, key=lambda x: x[1],
                              reverse=True)[:10]
        ax[i].bar(list(range(len(sorted_words))),
                  list(map(lambda x: x[1], sorted_words)))
        ax[i].set_title(book)
        ax[i].set_xlabel('Word index')
        ax[i].set_ylabel('Word frequency')
    plt.subplots_adjust(top=0.90)


def get_novel(url):
    response = request.urlopen(url)
    return response.read().decode('utf8')


def main():
    novel_url_list = [
        # Social Contract & Discourses, by Jean-Jacques Rousseau
        ('https://www.gutenberg.org/files/46333/46333-0.txt',
         'Social Contract & Discourses, by Jean-Jacques Rousseau'),
        # The Republic of Plato
        ('http://www.gutenberg.org/cache/epub/55201/pg55201.txt',
         'The Republic of Plato'),
        # The Clouds, by Aristophanes
        ('http://www.gutenberg.org/cache/epub/2562/pg2562.txt',
         'The Clouds, by Aristophanes'),
    ]
    novel_tokens_list = []
    novel_fdist_list = []

    for url, book in novel_url_list:
        print('Loading', url)
        text = get_novel(url)
        tokens = nltk.word_tokenize(text)
        novel_tokens_list.append(tokens)
        novel_fdist_list.append((nltk.FreqDist(tokens), book))

    plot_freq_dists(novel_fdist_list)
    plot_most_freq_word(novel_fdist_list, remove_stop_word=True,
                        part_of_speech='NN')

    plt.show()


if __name__ == '__main__':
    main()
