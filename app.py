import streamlit as st
import joblib
import os

try:
    print("Loading model file...")
    print("File exists?", os.path.exists("similarity.joblib"))
    similarity = joblib.load("similarity.joblib")
    print("Model loaded successfully.")
except Exception as e:
    print("Model loading error:", e)


def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]

    distances = sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(movies_list.iloc[i[0]].title)

    return recommended_movies

movies_list = joblib.load('movies.joblib')
# similarity = joblib.load('similarity.joblib')

st.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #F6000;'>🎬 Welcome to Your Personalized Movie Recommender 🍿</h2git>
        <p style='font-size:18px; color: #AAAAAA;'>Discover your next favorite movie with the power of Machine Learning And Natural Language Processing.</p>
    </div>
""", unsafe_allow_html=True)

selected_movie_name = st.selectbox("Select a movie",(movies_list.title.values))

if st.button("Recommend"):

    recommendations = recommend(selected_movie_name)

    for i in recommendations:
        st.write("-",i)
