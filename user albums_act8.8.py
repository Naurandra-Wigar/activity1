def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album


while True:
    print("\nEnter album info (type 'q' to quit)")

    artist = input("Artist name: ")
    if artist == 'q':
        break

    title = input("Album title: ")
    if title == 'q':
        break

    album = make_album(artist, title)
    print(album)