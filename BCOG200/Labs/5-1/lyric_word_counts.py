'''
    usually we are writing complicated scripts that do a bunch of things. We usually want to divide them up into
    functions. That makes the program really clear, easy to edit, share, and fix. If you write complicated code,
    it can be very difficult to debug. Mistakes will creep in and you (or others) will have trouble finding them.

    It is common to have your program have an overall structure like the one below.
    - a main() function, and where the calling of the main function is the ONLY thing in your script that is global
        (except for import statements).
        this makes it easy to not accidentally get global/local variable mistakes.
        it is also nice because it means you can look at your main function, and the functions it calls, as an
        organized list of everything your program does.

    Examine the code below. Start by going to the bottom and finding the main function. Try to Follow the
    code by going through it in the order it will be executed.

    Comment the code to show that you understand what it is doing.
    This program, in addition to being structured in terms of functions, is keeping track of word counts differently
    from last week. How is it different?

    Then, add the functions that accomplish the following things:
    - checks to make sure the program's input argument (the directory passed to the program when it is run)
        - exists, and quits and prints an error message if not
        - has directories in it
    - checks to make sure that each artist directory has files in it, and quits and prints a message if not
    - checks to make sure that each song lyric file has at least one word in it
    - lower-cases each token
    - removes punctuation characters from the end of each token

    When writing this, keep in mind that that some of these objectives might reasonably be broken into multiple
    functions, to keep the code as tidy as possible.

    Also keep in mind where you call those functions from. For example, there are many places you could reasonably
    call a "remove_punctuation" function. But where is the "best" place to call it?
'''

import os
import string
import sys


def remove_hidden_files(directory_list):
    """
    Remove files whose names start with '.'.
    :param directory_list: All the files in a directory.
    :return: The list of valid (non hidden) files.
    """
    file_list = []
    for item in directory_list:
        if item[0] != '.':
            file_list.append(item)
    return file_list


def get_artist_list(input_directory):
    """
    Get all the artist names in the directory.
    :param input_directory: The path to the input directory.
    :return: The list of artist names.
    """
    directory_list = os.listdir(input_directory)
    artist_list = remove_hidden_files(directory_list)
    return artist_list


def get_song_lists(input_directory, artist_list):
    """
    Get a list of list of songs. Each sub list contains all the songs of an
    author.
    :param input_directory: The directory that contains
    :param artist_list: The list of artist names.
    :return: The list of list of song file names.
    """
    song_lists = []

    for artist in artist_list:
        artist_directory = input_directory + artist
        directory_list = os.listdir(artist_directory)
        song_list = remove_hidden_files(directory_list)
        song_lists.append(song_list)
    return song_lists


def lower_case_and_clean_word(words_in_song):
    """
    Lower case all the words and remove the punctuations.
    :param words_in_song: The list of words in a song
    :return: A list of words lower cased
    """
    exclude = set(string.punctuation)

    def clean_str(word):
        return ''.join(filter(lambda c: c not in exclude, word))

    return list(map(lambda s: clean_str(s.lower()), words_in_song))


def get_lyrics(input_directory, artist_list, song_lists):
    """
    Get all the lyrics for all the specified artist.
    :param input_directory: The directory contains the artists.
    :param artist_list: The list of artist names we care about.
    :param song_lists: The list of songs we care about
    :return: The list of list containing lyrics for songs of the specified
    artist.
    """
    lyric_lists = []
    num_artists = len(artist_list)
    for i in range(num_artists):

        artist = artist_list[i]
        song_list = song_lists[i]
        new_song_lyric_list = []

        for song in song_list:
            path = os.path.join(input_directory, artist)
            file_name = os.path.join(path, song)
            lyric_list = lower_case_and_clean_word(read_in_file(file_name))
            new_song_lyric_list.append(lyric_list)
        lyric_lists.append(new_song_lyric_list)

    return lyric_lists


def read_in_file(file_name):
    """
    Read in a song file and concatenate all the lines into one string. And then
    split up into words.
    :param file_name: The song file path.
    :return: A list of words in the file.
    """
    lyric_string = ""
    f = open(file_name)
    for line in f:
        line = line.strip('\n')
        lyric_string = lyric_string + " " + line
    f.close()
    lyric_list = lyric_string.split()
    return lyric_list


def count_single_song(token_list):
    """
    Count the frequency of each word in a file.
    :param token_list: The list of words (token)
    :return: A dictionary holding the frequency of each word.
    """
    freq_dict = {}
    for token in token_list:
        if token in freq_dict:
            freq_dict[token] += 1
        else:
            freq_dict[token] = 1
    return freq_dict


def count_all_songs(lyric_lists):
    """
    Count the word frequency of all the songs.
    :param lyric_lists: The list of list of tokens.
    :return: List of dictionaries to count for word freq.
    """
    num_artists = len(lyric_lists)
    freq_dict_lists = []
    for i in range(num_artists):
        current_songs = lyric_lists[i]
        num_songs = len(current_songs)
        freq_dict_list = []
        for j in range(num_songs):
            current_song = current_songs[j]
            freq_dict = count_single_song(current_song)
            freq_dict_list.append(freq_dict)
        freq_dict_lists.append(freq_dict_list)
    return freq_dict_lists


def get_num_types_lists(freq_dict_lists):
    """
    Get a list of list for number of unique words in a song
    :param freq_dict_lists: The word frequency counter for each song
    :return: The number of unique words in each song.
    """
    num_types_lists = []
    for i in range(len(freq_dict_lists)):
        current_artist = freq_dict_lists[i]
        artist_type_counts_list = []
        for j in range(len(current_artist)):
            current_song_dict = current_artist[j]
            num_types = len(current_song_dict)
            artist_type_counts_list.append(num_types)
        num_types_lists.append(artist_type_counts_list)
    return num_types_lists


def get_num_tokens_lists(lyric_lists):
    """
    Get a list of list for the number of words in each song
    :param lyric_lists: The list of song lyrics
    :return: The list of list for the number of words in each song
    """
    num_tokens_lists = []
    for i in range(len(lyric_lists)):
        current_artist = lyric_lists[i]
        artist_token_counts_list = []
        for j in range(len(current_artist)):
            current_song_list = current_artist[j]
            num_tokens = len(current_song_list)
            artist_token_counts_list.append(num_tokens)
        num_tokens_lists.append(artist_token_counts_list)
    return num_tokens_lists


def get_type_token_ratio_lists(num_tokens_lists, num_types_lists):
    """
    A list of list for the tt ratio of each song.
    :param num_tokens_lists: The list of list containing word count for each
                             song
    :param num_types_lists: The list of list containing unique word count for
                            each song
    :return: The tt ratio for each song
    """
    tt_ratio_lists = []
    for i in range(len(num_tokens_lists)):
        current_token_counts = num_tokens_lists[i]
        current_type_counts = num_types_lists[i]
        tt_ratio_list = []
        for j in range(len(current_token_counts)):
            tt_ratio = current_token_counts[j] / current_type_counts[j]
            tt_ratio_list.append(tt_ratio)
        tt_ratio_lists.append(tt_ratio_list)
    return tt_ratio_lists


def get_mean_tt_ratio(tt_ratio_lists):
    """
    Get the mean tt ratio for the artist
    :param tt_ratio_lists: The list of list of tt ratio for each song.
    :return: List of average tt ratio for each artist.
    """
    mean_tt_ratios = []
    num_artists = len(tt_ratio_lists)
    for i in range(num_artists):
        sum = 0
        num_songs = len(tt_ratio_lists[i])
        for j in range(num_songs):
            sum += tt_ratio_lists[i][j]
        mean = sum / num_songs
        mean_tt_ratios.append(mean)
    return mean_tt_ratios


def output_data(artist_list, mean_tt_ratios):
    """
    Print out the data in a nice format.
    :param artist_list: The list of artist names
    :param mean_tt_ratios: The mean tt ratio of the corresponding artist
    :return: None
    """
    num_artists = len(artist_list)
    print("Artist       TT Ratio")
    for i in range(num_artists):
        artist = artist_list[i]
        tt_ratio = mean_tt_ratios[i]
        print("{}       {:.2f}".format(artist, tt_ratio))


def get_input_dir():
    """
    Get the input dir from the command line.
    :return: The input dir path.
    """
    if len(sys.argv) > 1:
        input_dir = sys.argv[1]
        if os.path.isdir(input_dir):
            if len(os.listdir(input_dir)) > 0:
                return input_dir
    print('Invalid input dir')
    exit(1)


def validate_artist_dirs(input_dir, artist_list):
    """
    Check whether the artist dir has songs in it. Quit if not.
    :param input_dir: The input dir that contains the artist dirs
    :param artist_list: The list of artist dirs
    :return: None
    """
    for artist in artist_list:
        path = os.path.join(input_dir, artist)
        if len(remove_hidden_files(os.listdir(path))) == 0:
            print('Artist %s doesn\'t have any song in it' % artist)
            exit(1)


def validate_song_files(input_dir, artist_list):
    """
    Check to make sure each song file has at least one word
    :param input_dir: The dir contains all the artist dirs
    :param artist_list: The list of artists
    :return: None
    """
    for artist in artist_list:
        path = os.path.join(input_dir, artist)
        songs = remove_hidden_files(os.listdir(path))
        for song in songs:
            with open(os.path.join(path, song), 'r') as f:
                if len(f.read()) == 0:
                    print('Song %s from %s is empty' % (song, artist))
                    exit(1)


def main():
    """
    Main function.
    :return: None
    """
    input_directory = get_input_dir()
    artist_list = get_artist_list(input_directory)
    validate_artist_dirs(input_directory, artist_list)
    song_lists = get_song_lists(input_directory, artist_list)
    lyric_lists = get_lyrics(input_directory, artist_list, song_lists)
    freq_dict_lists = count_all_songs(lyric_lists)
    num_types_lists = get_num_types_lists(freq_dict_lists)
    num_tokens_lists = get_num_tokens_lists(lyric_lists)
    tt_ratio_lists = get_type_token_ratio_lists(num_tokens_lists,
                                                num_types_lists)
    mean_tt_ratios = get_mean_tt_ratio(tt_ratio_lists)
    output_data(artist_list, mean_tt_ratios)


main()
