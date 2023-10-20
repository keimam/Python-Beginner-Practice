def make_album(artist, album, songs=None):
    """Description Album"""

    des_album = {'name': artist, 'title': album}
    if songs:
        des_album['songs'] = songs

    return des_album

album1 = make_album(artist='ariel', album='mencari cinta', songs=13)
print(album1)
album2 = make_album('Luna', 'ingin kamu')
print(album2)