# Song-recommendation-System

This project implements a music recommender system using Streamlit as a web framework and the Spotify API (for retrieving album covers and song links).

Features:

Recommends similar songs based on a pre-computed similarity matrix.
Displays recommended songs with album covers.
Provides clickable links to open the songs on Spotify.

Requirements:
             Python 3.x
             Streamlit (pip install streamlit)
             Spotipy (pip install spotipy)

Pre-saved data files:
                     df.pkl: Contains song information (likely song name and artist).
                    similarity.pkl: Stores the similarity matrix for song recommendations.


Getting Started:

Clone the repository:

Bash
git clone https://github.com/<your-username>/music-recommender.git
Use code with caution.
Install dependencies:

Bash
pip install streamlit spotipy
Obtain Spotify API Credentials:

Create a Spotify developer account: https://developer.spotify.com/
Create a new app and note down your Client ID and Client Secret.
Replace Credentials:

Open the music_recommender.py file in a text editor.
Replace YOUR_CLIENT_ID with your actual Spotify Client ID.
Replace YOUR_CLIENT_SECRET with your actual Spotify Client Secret.
Run the app:

Open a terminal or command prompt and navigate to the project directory.

Run the following command:

Bash
streamlit run music_recommender.py
This will launch the Streamlit app in your web browser, typically at http://localhost:8501/.

Usage:

Select a song from the dropdown menu.
Click the "Show Recommendation" button.
View the recommended songs with album covers and click on the titles to open them on Spotify.
Note:

This code utilizes pre-computed data for recommendations. The process of generating the data (similarity matrix) is not included in this project.
Further Development:

Explore integrating Spotify Connect for in-app playback control (requires advanced development and adherence to Spotify's API terms).
Implement error handling for Spotify API calls.
