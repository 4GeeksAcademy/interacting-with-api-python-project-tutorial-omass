from dotenv import load_dotenv
load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pandas
import seaborn as sns

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


artist_id = '1ZwdS5xdxEREPySFridCfh'


credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
spotify = spotipy.Spotify(client_credentials_manager=credentials)
results = spotify.artist_top_tracks(artist_id)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])

    print()


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt


# Replace with your own Spotify API credentials
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'

# Initialize Spotipy with client credentials
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# Artist ID for Tupac
artist_id = "1ZwdS5xdxEREPySFridCfh"

# Get the top tracks for the artist
response = sp.artist_top_tracks(artist_id)

if response:
    # Extract relevant track information
    tracks = response["tracks"]
    tracks = [
        {
            "Track Name": track["name"],
            "Popularity": track["popularity"],
            "Duration (minutes)": (track["duration_ms"] / (1000 * 60)) % 60
        }
        for track in tracks
    ]

# Create a DataFrame from the track information
df = pd.DataFrame(tracks)

# Sort the DataFrame by increasing popularity
df_sorted = df.sort_values(by='Popularity')

# Display the top 3 songs by popularity with name, duration, and popularity
top_3_songs = df_sorted.head(3)
print(top_3_songs[['Track Name', 'Duration (minutes)', 'Popularity']])




# Create a DataFrame from the track information
df = pd.DataFrame(tracks)


# Create a scatter plot to analyze the relationship
plt.figure(figsize=(10, 6))
plt.scatter(df["Duration (minutes)"], df["Popularity"], c=df.index, cmap="Set1")
plt.title("Relationship Between Song Duration and Popularity")
plt.xlabel("Duration (minutes)")
plt.ylabel("Popularity")
plt.colorbar(label="Track Index")

# Show the scatter plot
plt.tight_layout()
plt.show()


plt.savefig('tracks.png')

print('tracks.png')

