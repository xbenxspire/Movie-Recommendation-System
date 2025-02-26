"""
Microservice A: Movie Quotes Service
-----------------------------------
Provides movie quotes information via REST API.
"""

import requests
from flask import Flask, request, jsonify
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='movie_quotes_service.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

app = Flask(__name__)

# Disable Flask's default output
import sys
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

API_URL = "https://quoteapi.pythonanywhere.com/quotes/"

# Fetch movie quotes data from external API
try:
    logging.info(f"Fetching movie quotes from {API_URL}")
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    quotes = data["Quotes"][0]
    logging.info(f"Successfully fetched {len(quotes)} movie quotes")
except requests.exceptions.RequestException as e:
    logging.error(f"Error fetching movie quotes: {str(e)}")
    quotes = []
    print("Error: Unable to retrieve movie quotes")

# Extract movie titles for quick lookup
movies = []
saved_movies = []
genre_count = {}

for num in range(len(quotes)):
    movies.append(quotes[num]["movie_title"])

@app.route('/')
def home():
    """Home route with API info"""
    logging.info(f"Received {request.method} request on {request.path}")
    return jsonify({
        "message": "Movie Quotes Service API",
        "endpoints": [
            "/get_movie_quote - Get movie quote information",
            "/health - Check service health"
        ]
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/get_movie_quote', methods=['GET'])
def query_movie_quotes():
    """Get movie quote information based on user input"""
    logging.info(f"Received {request.method} request on {request.path}")
    
    user_input = request.args.get('input')
    logging.info(f"User input: {user_input}")

    if user_input in movies:
        movie_index = movies.index(user_input)
        movie_data = quotes[movie_index]

        saved_movies.append({movies[movie_index]: movie_data["quote"]})

        if quotes[movie_index]["category"] not in genre_count:
            genre_count[movie_data["category"]] = 1
        else:
            genre_count[movie_data["category"]] += 1

        logging.info(f"Responding with data for movie: {user_input}")
        return jsonify(movie_data)

    elif user_input == "history":
        logging.info("Responding with history data")
        return jsonify(saved_movies)

    elif user_input == "stats":
        logging.info("Responding with stats data")
        return jsonify(genre_count)

    else:
        logging.warning(f"Movie not found: {user_input}")
        return jsonify({"error": "Movie does not exist in database"}), 404

if __name__ == '__main__':
    print("Movie Quotes Service")
    print("========================")
    print("Running on http://127.0.0.1:5004")
    app.run(host='127.0.0.1', port=5004, debug=False)
