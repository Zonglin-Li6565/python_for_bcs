import os
import sys
from typing import Dict, List


# STEP 1: Comment the main() function
# STEP 2: Complete the code for the eight class methods below that have no code.
#           Note: in this program we are keeping track of types and token
#           separately for each song, and then also
#           creating a type and token summary number for the artist that
#           combines all of their songs together.
#           Feel free to refer back to our code from earlier weeks. But you
#           will probably need to adapt it slightly
#           If you want to test yourself, coding it from scratch again is
#           good practice.
#           HINT: you dont need to count freqs, types, and tokens twice.
#           Do it for the songs
#           Then, combine the freq dictionaries for each song to create one
#           summary freq dictionary for the artist
#           Then you can count the artist's overall types and tokens from
#           that summary dictionary


class Artist:
    def __init__(self, name: str, directory_location: str) -> None:
        self.name: str = name
        self.directory_location: str = directory_location
        self.num_songs: int = 0
        self.song_list: List['Song'] = []
        self.lyric_freq_dict: Dict[str, int] = {}
        self._num_tokens: int = 0
        self._changed: bool = False

    def _update(self) -> None:
        """
        Lazy update. In case song is changed after added to the artist
        """
        if not self._changed:
            return
        self.lyric_freq_dict: Dict[str, int] = {}
        self._num_tokens = 0
        for song in self.song_list:
            song_dict = song.lyric_freq_dict
            for song_lyric in song_dict:
                self.lyric_freq_dict[song_lyric] = self.lyric_freq_dict.get(
                    song_lyric, 0) + song_dict[song_lyric]
            self._num_tokens += song.num_tokens
        self._changed = False

    @property
    def freq_dict(self) -> Dict[str, int]:
        self._update()
        return self.lyric_freq_dict

    @property
    def num_types(self) -> int:
        self._update()
        return len(self.lyric_freq_dict)

    @property
    def num_tokens(self) -> int:
        self._update()
        return self._num_tokens

    def add_song(self, song: 'Song') -> None:
        self.song_list.append(song)
        self._changed = True


class Song:
    def __init__(self, title: str, file_location: str) -> None:
        self.title: str = title
        self.file_location: str = file_location
        self.lyric_list: List[str] = []
        self.lyric_freq_dict: Dict[str, int] = {}

    @property
    def lyric(self) -> List[str]:
        return self.lyric_list

    @lyric.setter
    def lyric(self, lyric: str) -> None:
        lines = lyric.splitlines(keepends=False)
        for line in lines:
            line = line.lower().strip()
            words = line.split(' ')
            self.lyric_list += words
            for word in words:
                if word not in self.lyric_freq_dict:
                    self.lyric_freq_dict[word] = 0
                self.lyric_freq_dict[word] += 1

    @property
    def freq_dict(self) -> Dict[str, int]:
        return self.lyric_freq_dict

    @property
    def num_types(self) -> int:
        return len(self.lyric_freq_dict)

    @property
    def num_tokens(self) -> int:
        return len(self.lyric_list)


def remove_hidden_files(input_list: List[str]) -> List[str]:
    output_list = []
    for item in input_list:
        if item[0] != '.':
            output_list.append(item)
    return output_list


def main() -> None:
    # A list of artist object
    artist_object_list: List[Artist] = []
    # The input directory specified on the cmd line
    input_directory: str = sys.argv[1]
    # The files in the input directory
    artist_directory_list: List[str] = os.listdir(input_directory)
    # A list of artist names
    artist_list: List[str] = remove_hidden_files(artist_directory_list)

    for artist_name in artist_list:
        # Create the artist directory
        artist_directory = os.path.join(input_directory, artist_name)
        # Create a new instance of artist
        new_artist_instance = Artist(artist_name, artist_directory)
        # List of files in song directory
        song_directory_list = os.listdir(artist_directory)
        # Hidden files removed
        song_filename_list = remove_hidden_files(song_directory_list)

        for song_filename in song_filename_list:
            # Get the title of the song
            song_title = song_filename[:-4]
            # The full path of the song file
            song_location = os.path.join(artist_directory, song_filename)
            # Create a new instance of song
            new_song_instance = Song(song_title, song_location)
            # Add a new song to an artist
            new_artist_instance.add_song(new_song_instance)
            with open(song_location) as f:
                new_song_instance.lyric = f.read()

        # Add the artist to the list
        artist_object_list.append(new_artist_instance)

    # Print out the artists
    for i in range(len(artist_object_list)):
        artist = artist_object_list[i]
        print("{}     Types: {}      Tokens: {}".format(artist.name,
                                                        artist.num_types,
                                                        artist.num_tokens))
        for j in range(artist.num_songs):
            song = artist.song_list[j]
            print("     {}      Types: {}      Tokens: {}".format(
                song.title, song.num_types, song.num_tokens))


main()
