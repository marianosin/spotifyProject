from dotenv import dotenv_values
import base64
import requests


# Load the .env file
CLIENT_ID = dotenv_values(".env").get('SPOTIFY_API_CLIENT')
CLIENT_SECRET = dotenv_values(".env").get("SPOTIFY_API_SECRET")


# get Spotify API token

def get_spotify_token():
    # Encoding client id and secret
    auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    # Spotify API endpoint
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Make a POST request to the Spotify API
    response = requests.post(url, headers=headers, data=data)

    # Get the access token from the response
    access_token = response.json()['access_token']

    return access_token

def get_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }

def search_artist(artist_name, token):
    """
    Search for an artist on Spotify.

    Args:
        artist_name (str): The name of the artist to search for.
        token (str): The access token for the Spotify API.

    Returns:
        dict: A dictionary containing the JSON response from the Spotify API.
    """
    url = "https://api.spotify.com/v1/search"
    headers = get_headers(token)
    params = {
        "q": artist_name,
        "type": "artist"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def get_artist_albums(artist_id, token):
    """
    Retrieves the albums of a given artist from the Spotify API.

    Parameters:
    artist_id (str): The ID of the artist.
    token (str): The access token for the Spotify API.

    Returns:
    dict: A dictionary containing the response from the Spotify API in JSON format.
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
    headers = get_headers(token)
    response = requests.get(url, headers=headers)
    return response.json()
def get_artist_top_tracks(artist_id, token):
    """
    Retrieves the top tracks of a given artist from the Spotify API.

    Parameters:
    artist_id (str): The ID of the artist.
    token (str): The access token for the Spotify API.

    Returns:
    dict: A dictionary containing the response from the Spotify API in JSON format.
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
    headers = get_headers(token)
    params = {
        "country": "AR"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_artist_related_artists(artist_id, token):
    """
    Retrieves the related artists of a given artist from the Spotify API.

    Parameters:
    artist_id (str): The ID of the artist.
    token (str): The access token for the Spotify API.

    Returns:
    dict: A dictionary containing the response from the Spotify API in JSON format.
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/related-artists"
    headers = get_headers(token)
    response = requests.get(url, headers=headers)
    return response.json()

def check_saved_tracks(track_ids, token):
    """
    Checks if the current user has saved the specified tracks.

    Parameters:
    track_ids (list): A list of track IDs.
    token (str): The access token for the Spotify API.

    Returns:
    list: A list of boolean values indicating whether each track is saved or not.
    """
    url = "https://api.spotify.com/v1/me/tracks/contains"
    headers = get_headers(token)
    params = {
        "ids": ",".join(track_ids)
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def search_playlist(playlist_name, token):
    """
    Search for a playlist on Spotify.

    Args:
        playlist_name (str): The name of the playlist to search for.
        token (str): The access token for the Spotify API.

    Returns:
        dict: A dictionary containing the JSON response from the Spotify API.
    """
    url = "https://api.spotify.com/v1/search"
    headers = get_headers(token)
    params = {
        "q": playlist_name,
        "type": "playlist"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_playlist_tracks(playlist_id, token):
    """
    Retrieves the tracks of a given playlist from the Spotify API.

    Parameters:
    playlist_id (str): The ID of the playlist.
    token (str): The access token for the Spotify API.

    Returns:
    dict: A dictionary containing the response from the Spotify API in JSON format.
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_headers(token)
    response = requests.get(url, headers=headers)
    return response.json()

def get_user_followed_artists(token):
    """
    Retrieves the artists that the current user follows on Spotify.

    Parameters:
    token (str): The access token for the Spotify API.

    Returns:
    dict: A dictionary containing the response from the Spotify API in JSON format.
    """
    url = "https://api.spotify.com/v1/me/following"
    headers = get_headers(token)
    params = {
        "type": "artist"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()


