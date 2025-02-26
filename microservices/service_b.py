"""
Microservice B: Recommendation Engine Service
--------------------------------------------
Processes user preferences and generates personalized movie recommendations.
"""

from flask import Flask, request, jsonify
import json
import os
import logging
import random
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='recommendation_service.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s:%(message)s'
)

app = Flask(__name__)

# Disable Flask's default output
import sys
cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

# Path to data files
DATA_DIR = '../data'
MOVIES_FILE = os.path.join(DATA_DIR, 'movies.json')
PREFERENCES_FILE = os.path.join(DATA_DIR, 'preferences.json')
HISTORY_FILE = os.path.join(DATA_DIR, 'history.json')

def read_json_file(filename):
    """Read and parse a JSON file"""
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            logging.info(f"Read data from {filename}.")
            return data
    except FileNotFoundError:
        logging.error(f"File not found: {filename}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"JSON decode error in {filename}: {str(e)}")
        return {}

@app.route('/')
def home():
    """Home route with API info"""
    logging.info(f"Received {request.method} request on {request.path}")
    return jsonify({
        "message": "Recommendation Engine Service API",
        "endpoints": [
            "/recommend - Generate personalized recommendations",
            "/health - Check service health"
        ]
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/recommend', methods=['POST'])
def recommend_movies():
    """Generate personalized movie recommendations based on user preferences and history"""
    logging.info(f"Received recommendation request")
    
    try:
        if not request.is_json:
            logging.warning("Invalid Content-Type")
            return jsonify({"error": "Content-Type must be application/json"}), 400
        
        data = request.json
        user_id = data.get('user_id')
        if not user_id:
            return jsonify({"error": "user_id is required"}), 400
        
        # Get user preferences
        preferred_genres = data.get('preferred_genres', [])
        logging.info(f"User {user_id} preferences: {preferred_genres}")
        
        # Get all movies
        movies = read_json_file(MOVIES_FILE)
        if not movies:
            return jsonify({"error": "Could not read movies data"}), 500
        
        # Get user history
        history = read_json_file(HISTORY_FILE)
        user_history = history.get(str(user_id), [])
        watched_ids = [movie.get('id') for movie in user_history]
        
        # Filter out already watched movies
        unwatched_movies = [movie for movie in movies if movie['id'] not in watched_ids]
        
        # Generate recommendations
        recommendations = []
        
        # 1. First prioritize movies in preferred genres
        genre_matches = [
            movie for movie in unwatched_movies 
            if movie['genre'] in preferred_genres
        ]
        
        # Add a relevance score based on genre match
        scored_recommendations = []
        for movie in genre_matches:
            # Base score for genre match
            score = 0.8 + (random.random() * 0.2)  # Between 0.8 and 1.0
            scored_recommendations.append({
                "id": movie['id'],
                "title": movie['title'],
                "genre": movie['genre'],
                "release_date": movie['release_date'],
                "score": round(score, 2),
                "reason": f"Matches your preferred genre: {movie['genre']}"
            })
        
        # 2. If we don't have enough genre matches, add some random recommendations
        if len(scored_recommendations) < 5:
            # Get movies not in preferred genres
            other_movies = [
                movie for movie in unwatched_movies 
                if movie['genre'] not in preferred_genres
            ]
            
            # Randomly select some to fill up to 5 recommendations
            random.shuffle(other_movies)
            for movie in other_movies[:5 - len(scored_recommendations)]:
                # Lower score for non-genre match
                score = 0.5 + (random.random() * 0.3)  # Between 0.5 and 0.8
                scored_recommendations.append({
                    "id": movie['id'],
                    "title": movie['title'],
                    "genre": movie['genre'],
                    "release_date": movie['release_date'],
                    "score": round(score, 2),
                    "reason": "You might enjoy exploring this genre"
                })
        
        # Sort by score (highest first)
        scored_recommendations.sort(key=lambda x: x['score'], reverse=True)
        
        logging.info(f"Generated {len(scored_recommendations)} recommendations for user {user_id}")
        return jsonify({
            "user_id": user_id,
            "recommendations": scored_recommendations,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logging.error(f"Error generating recommendations: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"Starting Recommendation Engine Service on port 8001...")
    app.run(host='127.0.0.1', port=8001, debug=False)
