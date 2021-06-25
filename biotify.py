import spotipy
import time
import sys
from spotipy.oauth2 import SpotifyOAuth

args = sys.argv

if len(args) != 2:
    print('Usage: biotify twitter-username')

else:
    scope = "user-read-currently-playing"
    username = sys.argv[1]

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    while(1):
        result = sp.current_user_playing_track()
        print(result)
        if result:
            track = result['item']["name"]
            album = result['item']['album']['name']
            artist = result['item']['artists'][0]['name']

            pretty_str_playing = f"Currently listening : {track} - {album} by {artist}"

            print(pretty_str_playing)

        time.sleep(10)