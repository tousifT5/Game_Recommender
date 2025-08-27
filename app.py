import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import requests
import json
import time



## Files to import 

## vector method
# games_vector = np.load("pr_game_vector.npy")

data_path = "pr_game_data.csv"
## slice_similarity method
similarity_path = "pr_slice_similarity.npy"

rawg_api_key = st.secrets["RAWG_API_KEY"]

@st.cache_resource
def load_recommender_resources(data_path, similarity_path):
    data = pd.read_csv(data_path)
    # game_vectors = np.load(vectors_path)
    similarity = np.load(similarity_path)
    return data, similarity




def get_poster_path(game_title):
    url = 'https://api.rawg.io/api/games?key={}&search={}&page_size=3'.format(rawg_api_key,game_title.replace(" ","%20"))
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json().get("results")
        if result[0].get("background_image"):
            poster_path = result[0].get("background_image")
            return poster_path
        else:
            return placeholder_text(game_title)
    else:
        return "error while fetching poster" 


## placeholder.co is api through this we can find text images as per our needs
## base_url/hight*width/background_color/font_color.file_format?text="hello"&font_type
## example--> https://placehold.co/600x400/teal/000000.png?text=Elden%20Rings&font=roboto
def placeholder_text(game_title):
    # if len(game_title) > 10:
    #     title = game_title.replace(" ","|")
    #     print("https://placehold.co/200x230/teal/000000.png?text={}&font=roboto".format(title))

    return "https://placehold.co/200x230/teal/000000.png?text={}&font=roboto".format(game_title.replace(" ","%20"))


## vector method
# def recommender(name):
#     index = data[data["Title"] == name].index[0]
#     indexes = sorted(list(enumerate(cosine_similarity(games_vector[index].reshape(1,-1),games_vector)[0])),reverse=True,key=lambda x:x[1])[:8]
#     r_index = []
#     for i in  indexes:
#         r_index.append(i[0])
#     return r_index


## slice_similarity method
def recommender(name):
    index = data[data["Title"] == name].index[0]
    indexes = similarity[index][1:11]
    r_index = []
    for i in  indexes:
        r_index.append(i[0])
    return r_index

data , similarity = load_recommender_resources(data_path,similarity_path)
games_list = data["Title"].values



## Layout
st.header("Game Recommender System")

selected_game = st.selectbox(
    "Select Game",
    games_list,
    index=None,
    placeholder="Game",
)

button = st.button("Recommend")

if selected_game and button:
    recommended_index = recommender(selected_game)
    recommended_games = data.iloc[recommended_index]["Title"].values
    for game_title in recommended_games:
        # poster = get_poster(game)
        with st.container():
            st.title(game_title)
            st.image(get_poster_path(game_title),width=750)
        time.sleep(0.2)
        # st.write(get_poster_path(game))

