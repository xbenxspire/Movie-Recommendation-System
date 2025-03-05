"""
Movie Recommendation System Server
---------------------------------
A Flask-based REST API for tracking movies, managing watch history, and user preferences.
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import sys
import logging
from datetime import datetime
from werkzeug.serving import WSGIRequestHandler

# Configure logging to file
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

# Disable Flask's default logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

# Use HTTP/1.1 for better connection handling
WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Disable Flask's default output
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

# Create data directory in current working directory
DATA_DIR = 'data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# File paths for data storage
MOVIES_FILE = os.path.join(DATA_DIR, 'movies.json')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')
PREFERENCES_FILE = os.path.join(DATA_DIR, 'preferences.json')

# Sample movie data with popular genres from IMDb
SAMPLE_MOVIES = [
    # Action Movies
    {"id": 1, "title": "The Dark Knight", "genre": "Action", "release_date": "2008-07-18"},
    {"id": 2, "title": "Mad Max: Fury Road", "genre": "Action", "release_date": "2015-05-15"},
    {"id": 3, "title": "John Wick", "genre": "Action", "release_date": "2014-10-24"},
    {"id": 4, "title": "Avengers: Endgame", "genre": "Action", "release_date": "2019-04-26"},
    {"id": 5, "title": "Die Hard", "genre": "Action", "release_date": "1988-07-15"},
    
    # Drama Movies
    {"id": 6, "title": "The Shawshank Redemption", "genre": "Drama", "release_date": "1994-09-23"},
    {"id": 7, "title": "Forrest Gump", "genre": "Drama", "release_date": "1994-07-06"},
    {"id": 8, "title": "The Godfather", "genre": "Drama", "release_date": "1972-03-24"},
    {"id": 9, "title": "Schindler's List", "genre": "Drama", "release_date": "1993-12-15"},
    {"id": 10, "title": "The Green Mile", "genre": "Drama", "release_date": "1999-12-10"},
    
    # Sci-Fi Movies
    {"id": 11, "title": "Inception", "genre": "Sci-Fi", "release_date": "2010-07-16"},
    {"id": 12, "title": "The Matrix", "genre": "Sci-Fi", "release_date": "1999-03-31"},
    {"id": 13, "title": "Interstellar", "genre": "Sci-Fi", "release_date": "2014-11-07"},
    {"id": 14, "title": "Blade Runner 2049", "genre": "Sci-Fi", "release_date": "2017-10-06"},
    {"id": 15, "title": "Star Wars: Episode V - The Empire Strikes Back", "genre": "Sci-Fi", "release_date": "1980-05-21"},
    
    # Comedy Movies
    {"id": 16, "title": "The Hangover", "genre": "Comedy", "release_date": "2009-06-05"},
    {"id": 17, "title": "Superbad", "genre": "Comedy", "release_date": "2007-08-17"},
    {"id": 18, "title": "Bridesmaids", "genre": "Comedy", "release_date": "2011-05-13"},
    {"id": 19, "title": "The Grand Budapest Hotel", "genre": "Comedy", "release_date": "2014-03-28"},
    {"id": 20, "title": "Deadpool", "genre": "Comedy", "release_date": "2016-02-12"},
    
    # Horror Movies
    {"id": 21, "title": "The Conjuring", "genre": "Horror", "release_date": "2013-07-19"},
    {"id": 22, "title": "Get Out", "genre": "Horror", "release_date": "2017-02-24"},
    {"id": 23, "title": "A Quiet Place", "genre": "Horror", "release_date": "2018-04-06"},
    {"id": 24, "title": "The Shining", "genre": "Horror", "release_date": "1980-05-23"},
    {"id": 25, "title": "Hereditary", "genre": "Horror", "release_date": "2018-06-08"},
    
    # Romance Movies
    {"id": 26, "title": "The Notebook", "genre": "Romance", "release_date": "2004-06-25"},
    {"id": 27, "title": "La La Land", "genre": "Romance", "release_date": "2016-12-09"},
    {"id": 28, "title": "Titanic", "genre": "Romance", "release_date": "1997-12-19"},
    {"id": 29, "title": "Pride and Prejudice", "genre": "Romance", "release_date": "2005-09-16"},
    {"id": 30, "title": "Eternal Sunshine of the Spotless Mind", "genre": "Romance", "release_date": "2004-03-19"},
    
    # Crime Movies
    {"id": 31, "title": "Pulp Fiction", "genre": "Crime", "release_date": "1994-10-14"},
    {"id": 32, "title": "The Departed", "genre": "Crime", "release_date": "2006-10-06"},
    {"id": 33, "title": "The Godfather Part II", "genre": "Crime", "release_date": "1974-12-20"},
    {"id": 34, "title": "Goodfellas", "genre": "Crime", "release_date": "1990-09-19"},
    {"id": 35, "title": "No Country for Old Men", "genre": "Crime", "release_date": "2007-11-09"},
    
    # Animation Movies
    {"id": 36, "title": "Toy Story", "genre": "Animation", "release_date": "1995-11-22"},
    {"id": 37, "title": "Spirited Away", "genre": "Animation", "release_date": "2001-07-20"},
    {"id": 38, "title": "The Lion King", "genre": "Animation", "release_date": "1994-06-24"},
    {"id": 39, "title": "Spider-Man: Into the Spider-Verse", "genre": "Animation", "release_date": "2018-12-14"},
    {"id": 40, "title": "WALL-E", "genre": "Animation", "release_date": "2008-06-27"}
]

def init_storage():
    """Initialize storage files with default data"""
    # Initialize movies file
    if not os.path.exists(MOVIES_FILE):
        write_json_file(MOVIES_FILE, SAMPLE_MOVIES)
        logging.info(f"Initialized {MOVIES_FILE} with sample data.")
    
    # Initialize history file if it doesn't exist
    if not os.path.exists(HISTORY_FILE):
        write_json_file(HISTORY_FILE, {})
        logging.info(f"Initialized {HISTORY_FILE} with empty history.")
    
    # Initialize preferences file if it doesn't exist
    if not os.path.exists(PREFERENCES_FILE):
        write_json_file(PREFERENCES_FILE, {})
        logging.info(f"Initialized {PREFERENCES_FILE} with empty preferences.")

def read_json_file(filename):
    """Read and parse a JSON file"""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            logging.info(f"Read data from {filename}.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        if filename == MOVIES_FILE:
            return SAMPLE_MOVIES
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error in {filename}: {str(e)}")
        if filename == MOVIES_FILE:
            return SAMPLE_MOVIES
        return {}

def write_json_file(filename, data):
    """Write data to a JSON file"""
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            logging.info(f"Wrote data to {filename}.")
    except Exception as e:
        logging.error(f"Error writing to {filename}: {str(e)}")

@app.route('/')
def home():
    """Home route with API info"""
    logging.info(f"Received {request.method} request on {request.path}")
    return jsonify({
        "message": "Movie Recommendation API",
        "endpoints": [
            "/movies - List all movies",
            "/movies/search/<query> - Search movies",
            "/preferences/<user_id> - Save preferences",
            "/history/<user_id> - View history",
            "/history/<user_id>/<movie_id> - Add to history",
            "/history/<undo_token> - Undo last watch"
        ]
    })

@app.route('/movies', methods=['GET'])
def list_movies():
    """List all available movies"""
    logging.info(f"Received {request.method} request on {request.path} from {request.remote_addr}")
    try:
        movies = read_json_file(MOVIES_FILE)
        if not movies:  # If file is empty/corrupted, use sample data
            movies = SAMPLE_MOVIES
            write_json_file(MOVIES_FILE, SAMPLE_MOVIES)
            logging.info(f"{MOVIES_FILE} was empty or corrupted. Reinitialized with sample data.")
        logging.info(f"Returning {len(movies)} movies")
        response = jsonify(movies)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as e:
        logging.error(f"Error in list_movies: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/movies/search/<query>')
@app.route('/movies/search/<query>/', methods=['GET'])
def search_movies(query):
    """Search movies by title"""
    logging.info(f"Received {request.method} request on {request.path} with query: {query}")
    try:
        movies = read_json_file(MOVIES_FILE)
        if not movies:  # If file is empty/corrupted, use sample data
            movies = SAMPLE_MOVIES
            write_json_file(MOVIES_FILE, SAMPLE_MOVIES)
            logging.info(f"{MOVIES_FILE} was empty or corrupted. Reinitialized with sample data.")
            
        results = [
            movie for movie in movies 
            if query.lower() in movie["title"].lower()
        ]
        logging.info(f"Search query '{query}' returned {len(results)} results.")
        return jsonify(results)
    except Exception as e:
        logging.error(f"Error in search_movies: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/preferences/<int:user_id>', methods=['GET'])
@app.route('/preferences/<int:user_id>/', methods=['GET'])
def get_preferences(user_id):
    """Get user genre preferences"""
    logging.info(f"Received GET request on {request.path} for user_id: {user_id}")
    try:
        prefs = read_json_file(PREFERENCES_FILE)
        user_prefs = prefs.get(str(user_id), {})
        if isinstance(user_prefs, dict):
            # Normalize genre case to match movies.json
            preferred_genres = user_prefs.get('preferred_genres', [])
            movies = read_json_file(MOVIES_FILE)
            valid_genres = {movie['genre'] for movie in movies}
            normalized_genres = []
            for pref in preferred_genres:
                # Find matching genre ignoring case
                matching_genre = next(
                    (g for g in valid_genres if g.lower() == pref.lower()),
                    pref  # Keep original if no match found
                )
                normalized_genres.append(matching_genre)
            return jsonify({"preferred_genres": normalized_genres})
        return jsonify({"preferred_genres": []})
    except Exception as e:
        logging.error(f"Error getting preferences: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/preferences/<int:user_id>', methods=['POST'])
@app.route('/preferences/<int:user_id>/', methods=['POST'])
def save_preferences(user_id):
    """Save user genre preferences"""
    logging.info(f"Received POST request on {request.path} for user_id: {user_id}")
    try:
        if not request.is_json:
            logging.warning("Preferences: Invalid Content-Type")
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        # Get valid genres from movies.json
        movies = read_json_file(MOVIES_FILE)
        valid_genres = {movie['genre'] for movie in movies}
        
        # Normalize genre case to match movies.json
        preferred_genres = request.json.get('preferred_genres', [])
        normalized_genres = []
        invalid_genres = []
        
        for pref in preferred_genres:
            # Find matching genre ignoring case
            matching_genre = next(
                (g for g in valid_genres if g.lower() == pref.lower()),
                None
            )
            if matching_genre:
                normalized_genres.append(matching_genre)
            else:
                invalid_genres.append(pref)
        
        if invalid_genres:
            valid_genres_list = sorted(list(valid_genres))
            return jsonify({
                "error": f"Invalid genres: {', '.join(invalid_genres)}",
                "valid_genres": valid_genres_list
            }), 400
        
        prefs = read_json_file(PREFERENCES_FILE)
        prefs[str(user_id)] = {
            "preferred_genres": normalized_genres,
            "last_updated": datetime.now().isoformat()
        }
        write_json_file(PREFERENCES_FILE, prefs)
        logging.info(f"Saved preferences for user_id: {user_id}")
        return jsonify({"message": "Preferences saved successfully"})
    except Exception as e:
        logging.error(f"Error in save_preferences: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/history/<int:user_id>/<int:movie_id>', methods=['POST'])
@app.route('/history/<int:user_id>/<int:movie_id>/', methods=['POST'])
def add_to_history(user_id, movie_id):
    """Add a movie to user's watch history"""
    logging.info(f"Received {request.method} request on {request.path} for user_id: {user_id}, movie_id: {movie_id}")
    try:
        movies = read_json_file(MOVIES_FILE)
        if not movies:  # If file is empty/corrupted, use sample data
            movies = SAMPLE_MOVIES
            write_json_file(MOVIES_FILE, SAMPLE_MOVIES)
            logging.info(f"{MOVIES_FILE} was empty or corrupted. Reinitialized with sample data.")
            
        movie = next((m for m in movies if m["id"] == movie_id), None)
        if not movie:
            logging.warning(f"Add to history: Movie with id {movie_id} not found")
            return jsonify({"error": "Movie not found"}), 404
        
        history = read_json_file(HISTORY_FILE)
        movie_with_date = {**movie, "watched_date": datetime.now().isoformat()}
        
        if str(user_id) not in history:
            history[str(user_id)] = []
        
        history[str(user_id)].insert(0, movie_with_date)
        write_json_file(HISTORY_FILE, history)
        
        logging.info(f"Added movie id {movie_id} to history for user_id: {user_id}")
        return jsonify({
            "message": "Movie added to history",
            "undo_token": f"{user_id}:{movie_id}:{datetime.now().timestamp()}"
        })
    except Exception as e:
        logging.error(f"Error in add_to_history: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/history/<undo_token>', methods=['DELETE'])
@app.route('/history/<undo_token>/', methods=['DELETE'])
def undo_history(undo_token):
    """Remove last watched movie from history"""
    logging.info(f"Received {request.method} request on {request.path} with undo_token: {undo_token}")
    try:
        user_id, _, _ = undo_token.split(":")
        history = read_json_file(HISTORY_FILE)
        
        if str(user_id) in history and history[str(user_id)]:
            removed_movie = history[str(user_id)].pop(0)
            write_json_file(HISTORY_FILE, history)
            logging.info(f"Removed last watch entry for user_id: {user_id}")
            return jsonify({"message": "Last watch entry removed successfully"})
        
        logging.warning(f"Undo history: No history found for user_id: {user_id}")
        return jsonify({"error": "No history found"}), 404
    except Exception as e:
        logging.error(f"Error in undo_history: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/history/<int:user_id>', methods=['GET'])
@app.route('/history/<int:user_id>/', methods=['GET'])
def get_history(user_id):
    """Get user's watch history"""
    logging.info(f"Received {request.method} request on {request.path} for user_id: {user_id}")
    try:
        history = read_json_file(HISTORY_FILE)
        user_history = history.get(str(user_id), [])
        logging.info(f"Retrieved watch history for user_id: {user_id}, {len(user_history)} entries found.")
        return jsonify(user_history)
    except Exception as e:
        logging.error(f"Error in get_history: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logging.info("Setting up movie service...")
    print("Setting up movie service (takes about 5 seconds)...")
    init_storage()
    print("\nServer ready! Use the client window to interact with the service.")
    logging.info("Server setup complete. Starting Flask server.")
    
    # Start Flask server with minimal output
    app.run(host='127.0.0.1', port=8000, debug=False)
