import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=583e19c32a45c066ca7c5a994bef746a&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"  +  data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]

    recommend_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommended_movie_posters

movies_dict=pickle.load(open("movie_dict.pkl", "rb"))
movies=pd.DataFrame(movies_dict)
similarity= pickle.load(open("similarity.pkl", "rb"))
st.title('Movie Recommender')


selected_movie = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend Movie'):
    names,posters=recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])

