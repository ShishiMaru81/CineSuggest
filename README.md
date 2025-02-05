# CineSuggest


</h2>A Movie Recommendation System for all to use </h2>

Overview:

This is a Machine Learning-based Movie Recommendation System that suggests movies to users based on content similarity. The project utilizes TF-IDF Vectorization and cosine similarity to find movies similar to a given input. The system is deployed using Streamlit.

Features:

Provides movie recommendations based on content similarity.

Uses TF-IDF Vectorization to process movie metadata.

Implements cosine similarity for measuring closeness between movies.

Interactive user interface with Streamlit.

Efficient search mechanism using difflib for matching user input.

Saves trained model using Pickle for faster recommendations.

Technologies Used:

Python

-NumPy

-Pandas

-Scikit-learn

-Difflib

-Pickle

-Requests

-Streamlit

-TfidfVectorizer

-Dataset

The recommendation system uses a large CSV dataset containing metadata of movies, such as title, genre, description, and other relevant features.

git clone <"https://github.com/ShishiMaru81/CineSuggest">
cd CineSuggest
pip install -r requirements.txt
streamlit run app.py

Usages:

1.Enter a movie name in the input field.

2.The system will suggest the most similar movies.

3.Click on a suggested movie to explore more details.

Future Improvements:

-- Improve recommendation accuracy using deep learning models.

--Integrate a user-based collaborative filtering approach.

--Enhance the UI/UX with better visualization tools.

--Add support for real-time movie database updates.

---> Feel Free to use ,if you find any kind of issue please mail me paulanindya2001@gmail.com 

</>
