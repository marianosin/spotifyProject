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
        "Authorization": "Basic " + auth_base64.decode('utf-8'),
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials"
    }

    # Make a POST request to the Spotify API
    response = requests.post(url, headers=headers, data=data)

    # Get the access token from the response
    access_token = response.json()["access_token"]

    return access_token

