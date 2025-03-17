from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# IMDb Top 100 Movies API endpoint and headers
url = "https://imdb-top-100-movies.p.rapidapi.com/"
headers = {
    'x-rapidapi-key': "246d880ef4msh116aac3e8e35bd1p147958jsnaa4a4359235d",
    'x-rapidapi-host': "imdb-top-100-movies.p.rapidapi.com"
}

# Function to get top 100 movies
def get_top_movies():
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return "Failed to retrieve data."

# Function to search movies by name
def search_movies(movies, query):
    return [movie for movie in movies if query.lower() in movie['title'].lower()]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('search_query')
        movies = get_top_movies()
        if isinstance(movies, list):
            movies = search_movies(movies, query)
        return render_template('index4.html', movies=movies)
    else:
        movies = get_top_movies()
        return render_template('index4.html', movies=movies)

if __name__ == '__main__':
    app.run()
