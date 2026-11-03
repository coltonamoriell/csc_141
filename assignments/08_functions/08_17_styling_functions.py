def make_sandwich(*items):
    """Print a summary of the sandwich being ordered with given items."""
    print('\nMaking a sandwich with the following items:')
    for item in items:
        print(f'- {item}')


# Example usage
make_sandwich('turkey', 'swiss cheese', 'lettuce', 'mayo')






def make_album(artist_name, album_title, songs=None):
    """Return a dictionary describing a music album."""
    album = {
        'artist': artist_name.title(),
        'album': album_title.title(),
    }
    
    if songs:
        album['songs'] = songs
        
    return album


# Example usage
album_info = make_album('pink floyd', 'the dark side of the moon', songs=10)
print(album_info)