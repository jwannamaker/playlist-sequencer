import json
import spotipy
# from spotipy_anon import SpotifyAnon

# sp = spotipy.Spotify(auth_manager=SpotifyAnon())
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])


user = 'johnny.exe'
client_id = '8f412453485c4c5bb2e1c09d1f02c045'
client_secret = 'e784fb62d61d4c4ebf93554b0afb39a3'
redirect_uri = 'http://google.com/callback/'

oauth_object = spotipy.SpotifyOAuth(client_id, client_secret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotify_object = spotipy.Spotify(auth=token)
user_name = spotify_object.current_user()

# To print the response in readable format.
print(json.dumps(user_name, sort_keys=True, indent=4))
