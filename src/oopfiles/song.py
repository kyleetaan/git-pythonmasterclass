class Song:
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
        if artist is None:
            self.artist = Artist("Various Artists")
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
        if position is None:
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

def find_object(field, object_list):
    """ check object """
    for item in object_list:
        if item.name == field:
            return item
    return None

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # tuple 
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}: {}: {}: {}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            elif new_artist.name != artist_field:
                new_artist = find_object(artist_field, artist_list)
                
                if new_artist is None:
                    new_artist = Artist(artist_field)
                    artist_list.append(new_artist)
                new_album = None
            
            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
                new_artist.add_album(new_album)

            elif new_album.name != album_field:
                # We've just read a new album for the current artist
                # Retrieve the album object if there is one,
                # otherwise create a new album object and store it in the artist's collection.
                new_album = find_object(album_field, new_artist.albums)
                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                    new_artist.add_album(new_album)

            # create a new song object and add it to the current album's collection
            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)

    return artist_list
                

def create_checkfile(artist_list):
    """ create a check file from the object data """
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song),
                            file = checkfile)



if __name__ == "__main__":
    artist = load_data()
    print("There are {} artist".format(len(artist)))


    create_checkfile(artist)