import streamlit as st
import pandas as pd
import pickle
import difflib
import requests

# Load Data
Movies_dict = pickle.load(open("Movie_dict.pkl", "rb"))
Movies = pd.DataFrame(Movies_dict)
Similarity = pickle.load(open("similarity1.pkl", "rb"))


# Function to get movie posters using TMDb API
def fetch_poster(movie_title):
    """Fetch poster URL for a given movie title using TMDb API."""
    api_key = "YOUR_TMDB_API_KEY"  # Replace with your TMDb API key
    url = f"https://api.themoviedb.org/3/search/movie?api_key={"8265bd1679663a7ea12ac168da84d2e8"}&query={movie_title}"

    response = requests.get(url)
    data = response.json()

    if data["results"]:
        poster_path = data["results"][0]["poster_path"]
        full_poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}"
        return full_poster_url
    else:
        return "https://via.placeholder.com/200"  # Default placeholder if not found


def recommend(movie):
    """Recommend movies based on similarity and return posters."""

    Movie_List = Movies["title"].tolist()
    Find_close_match = difflib.get_close_matches(movie, Movie_List)

    if not Find_close_match:
        return ["No similar movies found."], ["https://via.placeholder.com/200"]

    close_match = Find_close_match[0]
    filtered_data = Movies[Movies["title"] == close_match]

    if filtered_data.empty:
        return ["Movie not found!"], ["https://via.placeholder.com/200"]

    close_index = filtered_data.index[0]

    similarity_score = list(enumerate(Similarity[close_index]))
    sorting_similarity = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommended_movies = []
    recommended_posters = []

    for i, (index, _) in enumerate(sorting_similarity[1:6]):  # Top 5 recommendations
        movie_title = Movies.iloc[index]["title"]
        recommended_movies.append(movie_title)
        recommended_posters.append(fetch_poster(movie_title))

    return recommended_movies, recommended_posters


# Streamlit UI
st.title("🎬 Movie Recommendation System")



st.markdown(
    """
    <style>
    .stApp {
        background-color: #ADD8E6;  
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App content
# st.title("🎬 Movie Recommendation System")
st.write("Welcome to the Movie Recommendation System! Choose a movie and get recommendations.")

name = st.text_input("Enter Your Name:")
email = st.text_input("Enter Your Email:")

selected_Movie_Name = st.selectbox(
    "🎬 Select a movie to get recommendations:",
    Movies["title"].values
)

if st.button("Recommend!"):
    recommended_movies, recommended_posters = recommend(selected_Movie_Name)

    if recommended_movies:
        st.subheader("Recommended Movies:")

        # Display movies and posters in a grid layout
        cols = st.columns(5)  # Create 5 columns for displaying posters

        for i in range(len(recommended_movies)):
            with cols[i]:  # Assign each movie to a column
                st.image(recommended_posters[i], use_column_width=True)
                st.write(recommended_movies[i])
st.markdown(
    """
    <style>
    .movie-poster:hover {
        transform: scale(1.1);  /* Scale up on hover */
        transition: transform 0.3s ease-in-out;  /* Smooth transition */
        border: 3px solid #FF6347;  /* Add border on hover */
    }
    .movie-poster {
        border-radius: 10px;  /* Optional: rounded corners */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h3 style='color: red;'>Created by Anindya Paul.</h3>", unsafe_allow_html=True)
github_url = "https://github.com/ShishiMaru81"  # Replace with your actual GitHub URL

# Create the button
if st.button("Visit My GitHub Profile"):
    # Open the GitHub profile when the button is clicked
    st.markdown(f'<a href="{github_url}" target="_blank">Click here to go to my GitHub</a>', unsafe_allow_html=True)



prompt=st.chat_input("Say Something About this Project!")

if prompt:
    st.write(f"User has sent a text : {prompt}")