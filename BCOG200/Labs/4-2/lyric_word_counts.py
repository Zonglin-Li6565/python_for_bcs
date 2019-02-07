'''
complete the program below, so that after you have two lists of files for two specified folders, the program
    1) creates an empty dictionary for artist
    2) adds that dictionary to the lyric dictionary list
    3) goes through each file in the artist's folder, counts the words in each file, and adds them to the appropriate
        dictionary
    4) prints out:
        - a list of the artists
        - their total number of songs
        - their total number of unique words
        - their total number of words overall
        like this:
            artist      songs       unique words       total words     unique word ratio
            swift       10          105                 986             9.10
            kanye       10          108                 751             7.54

'''

import os
import sys

if len(sys.argv) == 1 or (not os.path.isdir(sys.argv[1])):
    print('Provide a directory')
    exit(1)

folder_list = os.listdir(sys.argv[1])

lyric_dictionary_list = []

artist_name = []

for folder in filter(lambda s: not s.startswith('.'), folder_list):
    song_dir = os.path.join(sys.argv[1], folder)
    if not os.path.isdir(song_dir):
        continue
    artist = {'total_words': 1e-100, 'unique_words': set()}
    lyric_dictionary_list.append(artist)
    artist_name.append(folder)
    songs = os.listdir(song_dir)
    songs = list(filter(lambda s: s.endswith('.txt'), songs))
    artist['songs'] = len(songs)
    for song in songs:
        with open(os.path.join(song_dir, song), 'r') as song_f:
            for line in song_f:
                # TODO: Make be more intelligent when counting words
                words = line.split(' ')
                artist['total_words'] += len(words)
                artist['unique_words'] = artist['unique_words'].union(words)


def print_info(*args):
    print(('{:<20}' * len(args)).format(*args))


print_info('artist', 'songs', 'unique words', 'total words',
           'unique word ratio')

for i, artist in enumerate(artist_name):
    artist_dict = lyric_dictionary_list[i]
    total_words = artist_dict['total_words']
    songs = artist_dict['songs']
    unique_words = len(artist_dict['unique_words'])
    print_info(artist, songs, unique_words, int(total_words),
               '%.02f' % (unique_words / total_words))
