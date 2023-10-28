import os
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


st.title("楽曲検索ページ")
keyword = st.text_input("検索ワード")
num_mg = st.slider("検索数", 1, 10, 5)


if st.button("検索", key='button1'):
    if keyword == "":
        st.warning("検索ワードを入力してください")
    else:
        results = sp.search(q=keyword, limit=num_mg, market="JP")
        for idx, track in enumerate(results['tracks']['items']):
            st.write(idx + 1)
            col1, col2 = st.columns(2)
            col1.image(track['album']['images'][0]['url'], width=200)
            st.write(track['name'], "/", track['artists'][0]['name'])
            url = track['preview_url']
            if url is not None:
                col2.markdown(f'<iframe src="{url}" width=300 height=150></iframe>', unsafe_allow_html=True)
            else:
                col2.write("お聴きになることが出来ません")
            st.write(f"{track['name']}のURL：{track['album']['external_urls']['spotify']}")
