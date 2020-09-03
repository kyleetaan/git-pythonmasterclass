class Song():
    """ """

    def __init__(self, title, artist, duration=0):
        """  """
        self.title = title
        self.artist = artist
        self.duration = duration


class Album():
    """ Collection of songs

    Args:
        .... : ....
        .... : ....
        tracks (List[Song]): 
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist == None:
            self.artist = "Various Artists"
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Adds a song to the tracklist

        Args:
            song (Song): ...
            sdfdf: ....
            sdfsdf: ....
        """
        if position == None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """ Basic class to store artist details

    Attributes:
        name (str): .....
        albums (List[Album]): .....
    
    Methods:
        add_album: ...
    """

    def __init__(self, name):
        self.name = name
        self.albums = []
    
    def add_album(self, album):
        """ add a new album

        Args:
            album (Album): ...
        """
        self.albums.append(album)

def load_data():
    new_artist = None
    new_album = None
    artist_list = None

    with open("albums.txt", "r") as albums:
        for line in albums:
            # tuple 
            artist_field, album_field, year_field, song_field =tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

if __name__ == "__main__":
    load_data()