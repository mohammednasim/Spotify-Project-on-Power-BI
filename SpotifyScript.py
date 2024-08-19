import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Correct file path
file_path = 'E:\\PowerBiProjects\\spotifyProject\\spotify-2023.csv'

# Load the Spotify dataset
spotify_df = pd.read_csv(file_path, encoding='ISO-8859-1')

# Replace these with your Spotify API credentials
client_id = '9b8277c7e7aa4e45b749d1d735ba22a4'
client_secret = '90512e7914f747c0b80d4e5846175cfa'

# Set up Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_album_cover_url(track_name, artist_name):
    """
    Function to fetch the album cover URL for a given track and artist name using the Spotify API.
    """
    try:
        result = sp.search(q=f"track:{track_name} artist:{artist_name}", type='track', limit=1)
        if result['tracks']['items']:
            album_cover_url = result['tracks']['items'][0]['album']['images'][0]['url']
            return album_cover_url
        else:
            return None
    except Exception as e:
        print(f"Error fetching URL for {track_name} by {artist_name}: {e}")
        return None

# Apply the function to each row in the dataset
spotify_df['album_cover_url'] = spotify_df.apply(lambda row: get_album_cover_url(row['track_name'], row['artist(s)_name']), axis=1)

# Save the updated dataset with album cover URLs
output_file_path = 'E:\\PowerBiProjects\\spotifyProject\\spotify_with_cover_urls.csv'
spotify_df.to_csv(output_file_path, index=False)

print(f"Updated dataset saved to {output_file_path}")

