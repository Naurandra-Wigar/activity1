def make_album(artist, title, tracks=None):
    album = {"artist": artist, "title": title}
    if tracks:
        album["tracks"] = tracks
    return album


print(make_album("Adele", "21"))
print(make_album("Coldplay", "Parachutes"))
print(make_album("Ed Sheeran", "Divide"))
print(make_album("Adele", "21", tracks=11))   # dengan jumlah lagu