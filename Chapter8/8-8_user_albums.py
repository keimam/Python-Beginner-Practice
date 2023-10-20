def make_album(artist, title, tracks=0):
    """Description Album"""    
    album_dict = {
        'name': artist.title(), 
        'title': title.title()
        }
    
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict

title_prompt = f"\nWhat album are you thinking of: "
artist_prompt = f"Who's the artist? "

print("Enter 'q' at anytime to stop")

while True:
    title = input(title_prompt)
    if title == 'q':
        break
    
    artist = input(artist_prompt)
    if artist == 'q':
        break

    album = make_album(artist=artist, title=title)
    print(album)

print("\nThanks for responding")
