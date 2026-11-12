def make_album(artist_name, album_title, songs=None):
    """Return a dictionary describing a music album."""
    album = {
        'artist': artist_name.title(),
        'album': album_title.title()
    }
    if songs:
        album['songs'] = songs
    return album

# Prompt the user for input instructions
print("Welcome! Enter album details below.")
print("(enter 'q' at any time to quit)\n")

while True:
    artist_input = input("Artist name: ")
    if artist_input.lower() == 'q':
        break
        
    album_input = input("Album title: ")
    if album_input.lower() == 'q':
        break
        
 
    