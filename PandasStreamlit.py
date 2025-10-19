# Goal: Analyze a dataset and create a simple interactive web application to display the results.

# Part 1: G
# Choose a publicly available CSV dataset (e.g., a dataset on movie ratings, weather data, or sales records). Provide a link to the data file.
# Use Pandas to load the dataset into a DataFrame.
# Perform at least three data analysis tasks using Pandas methods, for example:

# Calculate the mean or median of a numeric column.
# Filter the data to find specific rows (e.g., all movies released after 2020).
# Group the data and perform an aggregation (e.g., find the average sales per region).
# Save the results of your analysis to a new CSV file.

# Part 2: VG
# Create a web application using Streamlit.
# The app should display the raw data from your CSV file in a table.
# Add a sidebar with widgets (e.g., a slider, a selectbox) that allows the user to interactively filter the data. For example, if you're using a movie dataset, the user should be able to filter by a range of years or a specific genre.
# Display one or more plots (e.g., a bar chart, a line chart) using a plotting library like Matplotlib or Altair, based on the filtered data. The plots should update in real time as the user interacts with the widgets.

#############################################################################################################

# **Part 1**
# Pandas manipulation

# Below is the link to the Kaggle Dataset that I used:
"https://www.kaggle.com/datasets/solomonameh/spotify-music-dataset?resource=download&select=high_popularity_spotify_data.csv"

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('/Users/zagozend/MyPythonJourney/Training/Läxor/high_popularity_spotify_data.csv')

# DATA CLEANING:

# We drop the columns we dont want to work with, only selecting a few.
df = df.drop_duplicates()

df = df.drop(columns=["type", "playlist_id", "id", "playlist_name", "track_album_id", "uri", "track_href", "analysis_url", "track_id", "key", "time_signature", "speechiness", "mode", "loudness", "liveness", "instrumentalness", "playlist_subgenre"])

# Check for values that are empty and filling them with information via fillna() method
df["track_album_name"] = df["track_album_name"].fillna("Single")

# Creates a new column to work with based on the "track_album_release_date" column to only get the years
df["track_album_release_date"] = pd.to_datetime(df["track_album_release_date"], errors="coerce", format="mixed")
df["year"] = df["track_album_release_date"].dt.year

#############################################################################################################

# Sidebar creation

st.sidebar.header("Filter through here")

# A selector for the different genres
genre_selector = st.sidebar.multiselect(
    "Select the genre(s):",
    options=df["playlist_genre"].unique(),
    default=df["playlist_genre"].unique()
)

# Selector for the different artists
artist_selector = st.sidebar.multiselect(
    "Select the aritst(s):",
    options=df["track_artist"].unique(),
    default=df["track_artist"].unique()
)

# Slider for all the years
year_range = st.sidebar.slider(
    "Select the year",
    int(df["year"].min()),
    int(df["year"].max()),
    (int(df["year"].min()), int(df["year"].max()))
)
# Some error handling when the selectors for genre and artists plots are empty 
if not genre_selector:
    genre_selector = df["playlist_genre"].unique()
if not artist_selector:
    artist_selector = df["track_artist"].unique()

# filter data for the interactable sidebar options
filtered_df = df[
    (df["playlist_genre"].isin(genre_selector)) &
    (df["track_artist"].isin(artist_selector)) &
    (df["year"].between(year_range[0], year_range[1]))
    
]
#############################################################################################################

# DATA ANALYSIS:

# Task 1
# Analysing the correlation between all the audio "stats" and what their correlation could mean for the popularity of the track
audio_correlation = filtered_df[["track_popularity","energy","tempo","danceability","acousticness","valence"]].corr()

# Task 2
# Analysing which genre is the most popular by checking the average
average_genre_popularity = filtered_df.groupby("playlist_genre")["track_popularity"].mean().sort_values(ascending=False)

# Task 3
# Seeing which years had the highest popularity based on all the info from the data 
music_trends = filtered_df.groupby("year")["track_popularity"].mean()

# Task 4
# Seeing which artists are the most popular
artist_average_popularity = filtered_df.groupby("track_artist")["track_popularity"].mean().sort_values(ascending=False).head(15)

#############################################################################################################
# **Part 2**
# Streamlit Designing

st.set_page_config(page_title="Music Popularity",
                   page_icon="🎵",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

st.title("🎵Music by popularity analysis🎵")

# Showcases only the top 10
st.subheader("Dataset Preview")
st.dataframe(df.head(10))

st.divider()
st.subheader("The Dataset Analysis", divider="violet")

# This part was done so that the x and y labels functioned properly, couldnt write my own names otherwise
average_genre_popularity_df = average_genre_popularity.reset_index()
average_genre_popularity_df.columns = ["Genre", "Popularity"]

artist_average_popularity_df = artist_average_popularity.reset_index()
artist_average_popularity_df.columns = ["Artist", "Popularity"]

music_trends_df = music_trends.reset_index()
music_trends_df.columns = ["Year", "Popularity"]

# Plot 1
fig_genre = px.bar(
    average_genre_popularity_df,
    x="Popularity",
    y="Genre",
    orientation="h",
    labels={"Popularity": "Popularity", "Genre": "Genre"}, #TODO: y label not appearing, fix it
    title="Average genre by popularity",
    color="Popularity",
    color_continuous_scale="tropic"
)
# Plot 2
fig_artists = px.bar(
    artist_average_popularity_df,
    x="Popularity",
    y="Artist",
    orientation="h",
    labels={"Popularity": "Popularity", "Artist": "Artist"}, #TODO: y label not appearing, fix it
    title="Top artist by popularity",
    color="Popularity",
    color_continuous_scale="tropic"
)
# Plot 3
fig_trends = px.line(
    music_trends_df,
    x="Year",
    y="Popularity",
    orientation="h",
    labels={"Years": "Years", "Popularity": "Popularity"}, #TODO: x label ("Years") not appearing, fix it
    title="Music trends over time"
    )
# Plot 4
fig_corr= px.imshow(
    audio_correlation,
    text_auto=True,
    color_continuous_scale="tropic",
    title="Audio features and popularity correlation"
)
# Organizing the plots in 2 different columns to fit perfectly on the streamlit website
left_column, right_column = st.columns(2)
# 2 on the left
with left_column:
    st.plotly_chart(fig_genre, use_container_width=True)
    st.plotly_chart(fig_trends, use_container_width=True)
# 2 on the right
with right_column:
    st.plotly_chart(fig_artists, use_container_width=True)
    st.plotly_chart(fig_corr, use_container_width=True)