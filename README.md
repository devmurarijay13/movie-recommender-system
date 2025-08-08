# 🎬 Movie Recommender System

A content-based movie recommendation system built using Python and Streamlit that suggests similar movies based on a given title. This project uses movie metadata, cosine similarity, and vectorization techniques to provide top 5 movie recommendations instantly through a web interface.

---

## 🚀 Demo

🖥️ Live App: https://movie-recommender-system-b885.onrender.com  
📂 GitHub: https://github.com/devmurarijay13/movie-recommender-system

---

## 📌 Project Overview

This project uses a content-based recommendation algorithm that computes the **cosine similarity** between movie descriptions to suggest similar titles. It reads preprocessed movie data and similarity scores stored in `.joblib` format and renders recommendations via a Streamlit web app.

---

## 🧠 Features

- Recommend 5 similar movies based on user input
- Uses precomputed cosine similarity
- Content-based filtering (based on genres, overview, etc.)
- Fast response using `joblib` serialized objects
- Clean UI using Streamlit

---

## 🛠️ Tech Stack

| Category          | Tools / Libraries               |
|-------------------|---------------------------------|
| Language          | Python                          |
| Libraries         | Pandas, Scikit-learn, Streamlit |
| Vectorization     | CountVectorizer / TF-IDF        |
| Similarity Metric | Cosine Similarity               |
| Deployment        | Streamlit                       |

---

## 📁 Project Structure 

movie-recommender-system/ <br>
├── app.py # Streamlit frontend <br>
├── movies.joblib # Movie metadata (title, poster, etc.) <br>
├── similarity.joblib # Precomputed cosine similarity matrix <br>
├── recommendation system.ipynb # Notebook with data processing & model <br> 
├── requirements.txt # Python dependencies <br>
└── README.md # Project documentation 

## 🧾 Dataset

Used a dataset of movies with metadata like:
- Title
- Overview
- Genres
- Keywords
- Cast & Crew

Preprocessing was done in the notebook: `recommendation system.ipynb`

---

## 🧮 Methodology

1. **Data Cleaning & Merging**
   - Extracted relevant metadata fields from TMDB dataset

2. **Feature Engineering**
   - Combined fields like genre, overview, keywords, cast into a single string

3. **Vectorization**
   - Used `CountVectorizer` or `TF-IDF Vectorizer` to convert text into numerical format

4. **Similarity Computation**
   - Calculated cosine similarity between movie vectors
   - Stored results in `similarity.joblib` for fast access

5. **Recommendation Logic**
   - When a user inputs a movie, the system fetches its vector and returns top 5 similar movies

---

🙋‍♂️ Author
Jay Devmurari
📧 devmurarijay66@gmail.com
