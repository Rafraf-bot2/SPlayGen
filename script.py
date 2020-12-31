import spotipy 
from spotipy.oauth2 import SpotifyOAuth
import json
import random

scope = 'playlist-modify-public user-top-read' 

f = open('username.txt', 'r').read()
token = SpotifyOAuth(scope=scope, username=f)

spotifyObject = spotipy.Spotify(auth_manager = token)

playlist_name = "bordel"
playlist_desc = "gros foutoir."

artist = spotifyObject.current_user_top_artists(limit=20,time_range='short_term')
topArtistIds = []
topArtistNames = []
randtracks = []
albumsTid = []

for i in range(len(artist["items"])):
    topArtistIds.append(artist["items"][i]["id"])
    topArtistNames.append(artist["items"][i]["name"])

with open('topArtists.txt', 'w') as fil:
    for item in topArtistNames:
        fil.write("%s\n" % item)

for i in range(len(topArtistIds)):
    albums = spotifyObject.artist_albums(limit=50, album_type="album",artist_id=topArtistIds[i])
    if(str(len(albums["items"])!=0)):
        for m in range(len(albums["items"])-1) :
            albumsTid.append(albums["items"][m]["id"])

    albums=spotifyObject.artist_albums(limit=50, album_type="single",artist_id=topArtistIds[i])
    if(str(len(albums["items"])!=0)):
        for m in range(len(albums["items"])-1) :
            albumsTid.append(albums["items"][m]["id"])

    for k in range(5):
        random.seed()
        x = random.randint(0, len(albumsTid)-1)
        albumID=albumsTid[x]
        track=spotifyObject.album_tracks(album_id=albumID)
        random.seed()
        y=random.randint(0, len(track["items"])-1)
        randtracks.append(track["items"][y]["id"])
    albumsTid.clear()

random.shuffle(randtracks)

preplaylist = spotifyObject.user_playlists(user=f)
j=0
exist = False
playlistID = "oeoeeooe"
while (j!=len(preplaylist["items"])  | (exist== False)) :
    if(preplaylist["items"][j]["name"]==playlist_name) :
        exist = True
        playlistID = preplaylist["items"][j]["id"]
    j+=1   

if (exist==False):
    spotifyObject.user_playlist_create(user=f,name=playlist_name, public=True, description=playlist_desc)
    preplaylist = spotifyObject.user_playlists(user=f)
    j=0
    while(j!=len(preplaylist["items"])):
        if(preplaylist["items"][j]["name"]==playlist_name):
            exist=True
            playlistID = preplaylist["items"][j]["id"]
        j+=1    

spotifyObject.playlist_replace_items(playlistID, randtracks)