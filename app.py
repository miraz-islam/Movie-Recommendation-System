import streamlit as st
import pandas as pd
import pickle
import requests

st.title("Movies Recomendation System")

def recommend(movie):
    movie_index =movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),reverse = True, key = lambda x:x[1])[1:6]
    recommended = []
    for i in movie_list:
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movie_list = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_list) 
similarity = pickle.load(open("similarity.pkl","rb"))

selectedName = st.selectbox(
    'Enter the movie name:',movies['title'].values
)

if st.button("Recommend"):
    recommendation = recommend(selectedName)
    for i in recommendation:
        st.write(i)