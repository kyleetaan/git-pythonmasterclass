from nested_data import albums

SONGS_LIST_INDEX = 3 #songslist place in the tuple
TITLE_OF_SONG = 1 #title of the song
while True:
    print("Please choose your album (invalid choice exits)")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))

    choice = int(input())
    print()
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        break
    
    print("Please choose a song (invalid choice exits)")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        print()
        print("Playing {}".format(songs_list[song_choice - 1][TITLE_OF_SONG]))
        
    print("=" * 40)
    print()

