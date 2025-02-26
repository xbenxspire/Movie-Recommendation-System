"""
Microservice D: Watch History Service
-----------------------------------
Tracks user viewing history and analyzes watching patterns.
"""

from flask import Flask, request, jsonify
import json
import os
import logging
from datetime import datetime
from collections import Counter, defaultdict

# Configure logging
logging.basicConfig(
    filename='watch_history_service.log',
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
        "message": "Watch History Service API",
        "endpoints": [
            "/history/<user_id> - Get user watch history",
            "/history/<user_id>/<movie_id> - Add movie to history",
            "/history/stats/<user_id> - Get user watching statistics",
            "/history/trends - Get overall watching trends",
            "/health - Check service health"
        ]
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/history/<int:user_id>', methods=['GET'])
def get_history(user_id):
    """Get user's watch history"""
    logging.info(f"Received request for user {user_id} history")
    
    try:
        # Get user history
        history = read_json_file(HISTORY_FILE)
        user_history = history.get(str(user_id), [])
        
        if not user_history:
            return jsonify({
                "user_id": user_id,
                "message": "No watch history found for this user",
                "history": []
            })
        
        logging.info(f"Retrieved {len(user_history)} history entries for user {user_id}")
        return jsonify({
            "user_id": user_id,
            "history": user_history,
            "count": len(user_history),
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logging.error(f"Error getting history: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/history/<int:user_id>/<int:movie_id>', methods=['POST'])
def add_to_history(user_id, movie_id):
    """Add a movie to user's watch history"""
    logging.info(f"Received request to add movie {movie_id} to user {user_id} history")
    
    try:
        # Get all movies
        movies = read_json_file(MOVIES_FILE)
        if not movies:
            return jsonify({"error": "Could not read movies data"}), 500
        
        # Find the movie
        movie = next((m for m in movies if m["id"] == movie_id), None)
        if not movie:
            return jsonify({"error": f"Movie with ID {movie_id} not found"}), 404
        
        # Get history data
        history = read_json_file(HISTORY_FILE)
        
        # Add watched date to movie
        movie_with_date = {**movie, "watched_date": datetime.now().isoformat()}
        
        # Initialize user history if not exists
        if str(user_id) not in history:
            history[str(user_id)] = []
        
        # Add to beginning of history (most recent first)
        history[str(user_id)].insert(0, movie_with_date)
        
        # Save updated history
        write_json_file(HISTORY_FILE, history)
        
        logging.info(f"Added movie {movie_id} to user {user_id} history")
        return jsonify({
            "message": f"Added '{movie['title']}' to watch history",
            "user_id": user_id,
            "movie": movie,
            "timestamp": datetime.now().isoformat()
        })
        
    except Exception as e:
        logging.error(f"Error adding to history: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/history/stats/<int:user_id>', methods=['GET'])
def get_history_stats(user_id):
    """Get detailed statistics about user's watching patterns"""
    logging.info(f"Received request for user {user_id} history stats")
    
    try:
        # Get user history
        history = read_json_file(HISTORY_FILE)
        user_history = history.get(str(user_id), [])
        
        if not user_history:
            return jsonify({
                "user_id": user_id,
                "message": "No watch history found for this user",
                "stats": {}
            })
        
        # Analyze genres
        genre_counts = Counter([movie['genre'] for movie in user_history if 'genre' in movie])
        
        # Analyze watch dates by month
        months = defaultdict(int)
        for movie in user_history:
            if 'watched_date' in movie:
                try:
                    date = datetime.fromisoformat(movie['watched_date'])
                    month_key = f"{date.year}-{date.month:02d}"
                    months[month_key] += 1
                except (ValueError, TypeError):
                    # Skip invalid dates
                    continue
        
        # Calculate average movies per month
        if months:
            avg_per_month = round(len(user_history) / len(months), 1)
        else:
            avg_per_month = 0
        
        # Format response
        stats = {
            "user_id": user_id,
            "total_watched": len(user_history),
            "genre_breakdown": [
                {"name": genre, "count": count, "percentage": round((count / len(user_history)) * 100, 1)}
                for genre, count in genre_counts.most_common()
            ],
            "favorite_genre": genre_counts.most_common(1)[0][0] if genre_counts else "Unknown",
            "monthly_activity": [
                {"month": month, "count": count}
                for month, count in sorted(months.items())
            ],
            "avg_movies_per_month": avg_per_month,
            "timestamp": datetime.now().isoformat()
        }
        
        logging.info(f"Generated stats for user {user_id}")
        return jsonify(stats)
        
    except Exception as e:
        logging.error(f"Error generating history stats: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/history/trends', methods=['GET'])
def get_watching_trends():
    """Get overall watching trends across all users"""
    logging.info(f"Received request for overall watching trends")
    
    try:
        # Get all history
        history = read_json_file(HISTORY_FILE)
        
        if not history:
            return jsonify({
                "message": "No watch history found",
                "trends": {}
            })
        
        # Collect all watched movies
        all_watched = []
        for user_id, movies in history.items():
            all_watched.extend(movies)
        
        if not all_watched:
            return jsonify({
                "message": "No watch history found",
                "trends": {}
            })
        
        # Count most watched movies
        movie_counts = Counter([movie['title'] for movie in all_watched if 'title' in movie])
        top_movies = movie_counts.most_common(5)
        
        # Count most watched genres
        genre_counts = Counter([movie['genre'] for movie in all_watched if 'genre' in movie])
        top_genres = genre_counts.most_common(5)
        
        # Analyze watch dates by month
        months = defaultdict(int)
        for movie in all_watched:
            if 'watched_date' in movie:
                try:
                    date = datetime.fromisoformat(movie['watched_date'])
                    month_key = f"{date.year}-{date.month:02d}"
                    months[month_key] += 1
                except (ValueError, TypeError):
                    # Skip invalid dates
                    continue
        
        # Format response
        trends = {
            "total_users": len(history),
            "total_watches": len(all_watched),
            "top_movies": [
                {"title": title, "count": count}
                for title, count in top_movies
            ],
            "top_genres": [
                {"name": genre, "count": count, "percentage": round((count / len(all_watched)) * 100, 1)}
                for genre, count in top_genres
            ],
            "monthly_activity": [
                {"month": month, "count": count}
                for month, count in sorted(months.items())
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        logging.info(f"Generated overall watching trends")
        return jsonify(trends)
        
    except Exception as e:
        logging.error(f"Error generating watching trends: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print(f"Starting Watch History Service on port 8003...")
    app.run(host='127.0.0.1', port=8003, debug=False)
