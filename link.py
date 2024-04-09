import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "ffdf830423f448da8b7e8312fa6bef58"
CLIENT_SECRET = "50bdd1dcd16541ecb862442bb963bdb4"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url)
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_uris = []
    recommended_music_posters = []
    artists = []
    for i in range(5):
        recommended_music_names.append(music.iloc[distances[i][0]]['song'])
        # fetch the Spotify URI
        artist = music.iloc[distances[i][0]]['artist']
        results = sp.search(q=f"track:{music.iloc[distances[i][0]]['song']} artist:{artist}", limit=1, type="track")
        if results and results["tracks"]["items"]:
            track = results["tracks"]["items"][0]
            uri = track["uri"]
            recommended_music_uris.append(uri)
        else:
            recommended_music_uris.append(None)

        # fetch the album cover image
        album_cover_url = get_song_album_cover_url(music.iloc[distances[i][0]]['song'], artist)
        recommended_music_posters.append(album_cover_url)

    return recommended_music_names, recommended_music_uris, recommended_music_posters

st.header('Music Recommender System')
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

music_list = music['song'].values
selected_movie = st.selectbox(
    "Type or select a song from the dropdown",
    music_list
)

if st.button('Show Recommendation'):
    recommended_music_names, recommended_music_uris, recommended_music_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5= st.columns(5)
    with col1:
        if recommended_music_uris[0]:
            st.markdown(f'[**{recommended_music_names[0]}**](spotify:track:{recommended_music_uris[0]})', unsafe_allow_html=True)
        else:
            st.markdown(f'**{recommended_music_names[0]}** (No results found)')
        st.image(recommended_music_posters[0])

    with col2:
        if recommended_music_uris[1]:
            st.markdown(f'[**{recommended_music_names[1]}**](spotify:track:{recommended_music_uris[1]})', unsafe_allow_html=True)
        else:
            st.markdown(f'**{recommended_music_names[1]}** (No results found)')
        st.image(recommended_music_posters[1])

    with col3:
        if recommended_music_uris[2]:
            st.markdown(f'[**{recommended_music_names[2]}**](spotify:track:{recommended_music_uris[2]})', unsafe_allow_html=True)
        else:
            st.markdown(f'**{recommended_music_names[2]}** (No results found)')
        st.image(recommended_music_posters[2])

    with col4:
        if recommended_music_uris[3]:
            st.markdown(f'[**{recommended_music_names[3]}**](spotify:track:{recommended_music_uris[3]})', unsafe_allow_html=True)
        else:
            st.markdown(f'**{recommended_music_names[3]}** (No results found)')
        st.image(recommended_music_posters[3])

    with col5:
        if recommended_music_uris[4]:
            st.markdown(f'[**{recommended_music_names[4]}**](spotify:track:{recommended_music_uris[4]})', unsafe_allow_html=True)
        else:
            st.markdown(f'**{recommended_music_names[4]}** (No results found)')
        st.image(recommended_music_posters[4])