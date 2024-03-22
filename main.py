from src import spotify


# Get playlist from Spotify
playlists = spotify.search_playlist('Los 40 Principales: Exitos 2024 | Lista 40', spotify.get_spotify_token())

#select the desired playlist
for playlist in playlists['playlists']['items']:
    if "Los 40 Principales: Exitos 2024 | Lista 40" ==playlist['name']:
        top_list = playlist.copy()
        break

playlist_id = top_list['tracks']['href'].split('/')[-2]

# Get tracks from playlist
tracks = spotify.get_playlist_tracks(playlist_id, spotify.get_spotify_token())


print('ok')