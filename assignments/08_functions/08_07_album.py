def make_album(artist_name, album_title, songs=None):
    """Return a dictionary describing a music album."""
    album = {
        'artist': artist_name.title(),
        'album': album_title.title()
    }
    if songs:
        album['songs'] = songs
    return album

# Create three dictionaries representing different albums (without song counts)
album1 = make_album('pink floyd', 'the dark side of the moon')
album2 = make_album('michael jackson', 'thriller')
album3 = make_album('daft punk', 'random access memories')

print(album1)
print(album2)
print(album3)

