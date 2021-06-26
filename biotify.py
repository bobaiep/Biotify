import spotipy
from time import sleep
from spotipy.oauth2 import SpotifyOAuth
from rauth import OAuth1Service
import os

class biotify:
    def __init__(self) -> None:
        self.spotify_api_auth = self.get_spotify_auth()
        self.twitter_api_oauth = self.get_twitter_oauth()
        self.default_bio = self.get_bio()
        self.current_bio = self.default_bio

    def get_spotify_auth(self):
        scope = "user-read-currently-playing"
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

        return sp

    def get_twitter_oauth(self):
        twitter = OAuth1Service(
            name='twitter',
            consumer_key=os.environ.get("TWITTER_API_KEY"),
            consumer_secret=os.environ.get("TWITTER_API_SECRET"),
            request_token_url='https://api.twitter.com/oauth/request_token',
            access_token_url='https://api.twitter.com/oauth/access_token',
            authorize_url='https://api.twitter.com/oauth/authorize',
            base_url='https://api.twitter.com/1.1/')

        request_token, request_token_secret = twitter.get_request_token(data={'oauth_callback': 'oob'})
        authorize_url = twitter.get_authorize_url(request_token)

        print('Visit this URL in your browser: ' + authorize_url)
        pin = input('Enter PIN from browser: ')

        session = twitter.get_auth_session(request_token,request_token_secret,method='POST',data={'oauth_verifier': pin})

        return session

    def get_bio(self):
        response = self.twitter_api_oauth.post("https://api.twitter.com/1.1/account/update_profile.json",data={},params={})
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )
        json_response = response.json()
        bio = json_response["description"]

        print(f"Your Bio : {bio}\n")

        return bio

    def set_bio(self,desc):
        params = {'description': desc} 
        response = self.twitter_api_oauth.post("https://api.twitter.com/1.1/account/update_profile.json",data={},params=params)
        if response.status_code != 200:
            raise Exception(
                "Request returned an error: {} {}".format(
                    response.status_code, response.text
                )
            )

    def run(self):
        last_track = ""
        idle_time = 0
        boo = 0
        while(1):
            result = self.spotify_api_auth.current_user_playing_track()
            if result:
                track = result['item']["name"]
                #album = result['item']['album']['name']
                artist = result['item']['artists'][0]['name']

                pretty_str_playing = f"Currently listening : {track} - {artist}"
                
                if last_track != track and result["is_playing"]:
                    boo = 0
                    idle_time = 0
                    self.current_bio = self.default_bio + "\n" + pretty_str_playing
                    sleep(0.5)
                    self.set_bio(self.current_bio)
                    print(pretty_str_playing)
                elif boo != 1 and not result["is_playing"]:
                    if idle_time > 30:
                        idle_time = 0
                        last_track = ""
                        boo = 1
                    else:
                        idle_time += 1
                elif boo == 1 and idle_time != -1:
                    print("Idlinng for more than 5min, setting the default bio back !")
                    sleep(0.5)
                    self.set_bio(self.default_bio)
                    idle_time = -1

                last_track = track
            else:
                if boo == 0 and last_track != "":
                    boo = 2
                    print("Idling or Error, setting the default bio back !")
                    sleep(0.5)
                    self.set_bio(self.default_bio)

            sleep(10)

if __name__ == '__main__' :
    session = biotify()
    try :
        session.run()
    except Exception as err:
        print("[Error] {}".format(err))
        print("Setting the default bio back !")
        print("Thank you for using biotify, see you soon !")
        session.set_bio(session.default_bio)
    except KeyboardInterrupt:
        print("Setting the default bio back !")
        print("Thank you for using biotify, see you soon !")
        session.set_bio(session.default_bio)