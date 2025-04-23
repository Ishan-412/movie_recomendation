from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load your movie and rating data
movies_df = pd.read_csv("movies.csv")
ratings_df = pd.read_csv("ratings.csv")

# Merge the two datasets on 'movieId'
movie_data = pd.merge(movies_df, ratings_df, on="movieId")

# Function to recommend top-rated movies in a given genre
def recommend_movies(genre):
    # Filter for rows that contain the genre (case insensitive)
    genre_movies = movie_data[movie_data['genres'].str.contains(genre, case=False, na=False)]

    # Group by movie title and calculate average rating
    top_movies = (
        genre_movies.groupby('title')['rating']
        .mean()
        .sort_values(ascending=False)
        .head(5)
    )

    # Return the list of top movie titles
    return top_movies.index.tolist()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    genre = data.get("genre")

    if not genre:
        return jsonify([])

    recommendations = recommend_movies(genre)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
