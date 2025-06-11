import streamlit as st
import joblib
import os

os.environ['PORT'] = '8501'

# ✅ Use Streamlit cache to load large files once and keep them in memory
@st.cache_resource
def load_similarity():
    return joblib.load("similarity.joblib")

@st.cache_data
def load_movies():
    return joblib.load("movies.joblib")

# Load the heavy files only once using cache
similarity = load_similarity()
movies_list = load_movies()

# 🎯 Recommendation logic
def recommend(movie):
    movie_index = movies_list[movies_list['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])
    recommended_movies = [movies_list.iloc[i[0]].title for i in distances[1:6]]
    return recommended_movies

# 🎨 UI
st.markdown("""
    <div style='text-align: center;'>
        <h2 style='color: #F6000;'>🎬 Welcome to Your Personalized Movie Recommender 🍿</h2>
        <p style='font-size:18px; color: #AAAAAA;'>Discover your next favorite movie with the power of Machine Learning and Natural Language Processing.</p>
    </div>
""", unsafe_allow_html=True)

selected_movie_name = st.selectbox("Select a movie", movies_list.title.values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write("-", i)
