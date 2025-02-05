"""
Movie Recommendation System Client
--------------------------------
An interactive command-line interface for the movie recommendation system.
"""

import cmd
import requests
import json
from datetime import datetime
from typing import List, Optional
from urllib.parse import quote

class MovieCLI(cmd.Cmd):
    """Interactive CLI for movie recommendation system"""
    
    intro = """
Welcome to the Movie Recommendation System!
Discover and get personalized movie recommendations you'll love.

⏱️  Quick commands - each takes <1 second to run

Available Commands:
  movies        - List all available movies
  search <title> - Search for movies (e.g., search "Dark Knight")
  watch <ids>   - Add movies to history (e.g., watch 1 or watch 1 2 3)
  history      - View your watch history
  genres       - List all available genres
  preferences  - View movies filtered by your preferences
  set preferences <genres> - Set your genre preferences
  remove preferences <genres> - Remove specific genre preferences
  help         - Show detailed help for commands
  quit/exit    - Exit the program

Type 'help <command>' for more details about a specific command.
"""
    prompt = 'Command: '
    
    def __init__(self):
        """Initialize CLI with base URL and current user"""
        super().__init__()
        self.base_url = "http://127.0.0.1:8000"  # Use 127.0.0.1 instead of localhost
        self.current_user = 1  # Simplified for demo
        self.session = requests.Session()  # Use session for connection pooling

    def show_available_commands(self):
        """Show available commands to help users navigate"""
        print("\nAvailable commands:")
        print("  movies          - List all available movies")
        print("  search <title>  - Search for movies")
        print("  genres          - List all available genres")
        print("  set preferences <genres> - Set your genre preferences")
        print("  remove preferences <genres> - Remove genre preferences")
        print("  preferences     - View movies in your preferred genres")
        print("  watch <ids>     - Add movies to history (e.g., watch 1 2 3)")
        print("  history         - View watch history")
        print("  help            - Show detailed help")
        print("  quit/exit       - Exit the program")
        print("\nType 'help <command>' for more details about a command.")

    def do_movies(self, arg):
        """List all available movies
        
        Usage: movies
        """
        try:
            response = self.session.get(f"{self.base_url}/movies", headers={'Accept': 'application/json'})
            if response.status_code == 404:
                print("Error: Could not connect to movies endpoint")
                print("Make sure the server is running and try again")
                return
            response.raise_for_status()
            
            movies = response.json()
            print("\nAvailable Movies:")
            print("-" * 50)
            for movie in movies:
                print(f"ID: {movie['id']}")
                print(f"Title: {movie['title']}")
                print(f"Genre: {movie['genre']}")
                print(f"Release Date: {movie['release_date']}")
                print("-" * 50)
            
            print("\nTip: Use 'watch <movie_id>' to add to history")
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_search(self, arg):
        """Search for movies by title
        
        Usage: search <movie title>
        Example: search "Dark Knight"
        """
        if not arg:
            print("Please provide a search term")
            self.show_available_commands()
            return
            
        try:
            encoded_query = quote(arg)
            response = self.session.get(f"{self.base_url}/movies/search/{encoded_query}")
            response.raise_for_status()
            
            movies = response.json()
            if movies:
                print("\nSearch Results:")
                print("-" * 50)
                for movie in movies:
                    print(f"ID: {movie['id']}")
                    print(f"Title: {movie['title']}")
                    print(f"Genre: {movie['genre']}")
                    print(f"Release Date: {movie['release_date']}")
                    print("-" * 50)
                
                print("\nTip: Use 'watch <movie_id>' to add to history")
            else:
                print("No movies found matching your search.")
                print("Try: searching by partial title or use 'movies' to see all available movies")
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_set(self, arg):
        """Set your genre preferences
        
        Usage: set preferences <genre1> <genre2> ...
        Example: set preferences Action Sci-Fi
        """
        args = arg.split()
        if not args or args[0] != 'preferences':
            print("Usage: set preferences <genre1> <genre2> ...")
            print("Example: set preferences Action Sci-Fi")
            self.show_available_commands()
            return
        
        # Remove 'preferences' from args
        genres = args[1:]
        if not genres:
            print("Please provide genre preferences")
            self.show_available_commands()
            return
            
        try:
            data = {
                "preferred_genres": genres
            }
            response = self.session.post(
                f"{self.base_url}/preferences/{self.current_user}",
                json=data
            )
            response.raise_for_status()
            
            result = response.json()
            if response.status_code == 400 and 'valid_genres' in result:
                print(f"Error: {result.get('error')}")
                print("\nValid genres are:")
                for genre in result['valid_genres']:
                    print(f"- {genre}")
                print("\nTip: Genre names are case-insensitive (e.g., 'action' = 'Action')")
            else:
                print(result.get('message', 'Preferences saved successfully!'))
                print("Use 'preferences' to view movies in your preferred genres")
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_remove(self, arg):
        """Remove specific genre preferences
        
        Usage: remove preferences <genre1> <genre2> ...
        Example: remove preferences Horror Comedy
        """
        args = arg.split()
        if not args or args[0] != 'preferences':
            print("Usage: remove preferences <genre1> <genre2> ...")
            print("Example: remove preferences Horror Comedy")
            self.show_available_commands()
            return
        
        # Remove 'preferences' from args
        genres_to_remove = set(args[1:])
        if not genres_to_remove:
            print("Please provide genres to remove")
            self.show_available_commands()
            return
            
        try:
            # Get current preferences
            response = self.session.get(f"{self.base_url}/preferences/{self.current_user}")
            response.raise_for_status()
            current_prefs = response.json().get('preferred_genres', [])
            
            # Remove specified genres (case-insensitive)
            updated_prefs = [g for g in current_prefs if not any(r.lower() == g.lower() for r in genres_to_remove)]
            
            # Update preferences
            data = {
                "preferred_genres": updated_prefs
            }
            response = self.session.post(
                f"{self.base_url}/preferences/{self.current_user}",
                json=data
            )
            response.raise_for_status()
            
            print(f"Removed preferences: {', '.join(genres_to_remove)}")
            if updated_prefs:
                print(f"Current preferences: {', '.join(updated_prefs)}")
            else:
                print("No preferences remaining")
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_preferences(self, arg):
        """View movies filtered by your preferences
        
        Usage: preferences
        """
        if arg:
            print("Usage: preferences")
            print("To set preferences, use: set preferences <genre1> <genre2> ...")
            print("To remove preferences, use: remove preferences <genre1> <genre2> ...")
            self.show_available_commands()
            return
        try:
            # Get user preferences
            response = self.session.get(f"{self.base_url}/preferences/{self.current_user}")
            response.raise_for_status()
            data = response.json()
            preferred_genres = data.get('preferred_genres', [])
            
            if not preferred_genres:
                print("No genre preferences set.")
                print("\nTips:")
                print("1. Use 'genres' to see available genres")
                print("2. Set preferences with: set preferences <genre1> <genre2> ...")
                print("   Example: set preferences Action Sci-Fi")
                print("   Note: Genre names are case-insensitive (e.g., 'action' = 'Action')")
                self.show_available_commands()
                return
            
            # Get all movies
            response = self.session.get(f"{self.base_url}/movies")
            response.raise_for_status()
            all_movies = response.json()
            
            # Filter movies by preferred genres
            filtered_movies = [m for m in all_movies if m['genre'] in preferred_genres]
            
            if filtered_movies:
                print(f"\nMovies in your preferred genres ({', '.join(preferred_genres)}):")
                print("-" * 50)
                for genre in preferred_genres:
                    genre_movies = [m for m in filtered_movies if m['genre'] == genre]
                    if genre_movies:
                        print(f"\n{genre} Movies:")
                        print("-" * 25)
                        for movie in genre_movies:
                            print(f"ID: {movie['id']}")
                            print(f"Title: {movie['title']}")
                            print(f"Release Date: {movie['release_date']}")
                            print("-" * 25)
            else:
                print("\nNo movies found in your preferred genres.")
                print("\nTips:")
                print("1. Use 'genres' to see available genres")
                print("2. Update preferences with: set preferences <genre1> <genre2> ...")
                print("   Example: set preferences Action Sci-Fi")
                print("   Note: Genre names are case-insensitive (e.g., 'action' = 'Action')")
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_watch(self, arg):
        """Add movies to your watch history
        
        Usage: watch <movie_id1> [movie_id2 movie_id3 ...]
        Examples: 
          watch 1
          watch 1 2 3
        """
        if not arg:
            print("Please provide at least one movie ID")
            self.show_available_commands()
            return
            
        movie_ids = []
        for id_str in arg.split():
            if not id_str.isdigit():
                print(f"Invalid movie ID: {id_str}")
                self.show_available_commands()
                return
            movie_ids.append(int(id_str))
            
        for movie_id in movie_ids:
            try:
                response = self.session.post(
                    f"{self.base_url}/history/{self.current_user}/{movie_id}"
                )
                response.raise_for_status()
                
                result = response.json()
                print(f"Movie {movie_id}: {result.get('message', 'Added to history!')}")
            except requests.exceptions.HTTPError as e:
                print(f"Movie {movie_id} - Server error: {e.response.status_code}")
                if e.response.text:
                    try:
                        error_data = e.response.json()
                        print(f"Error details: {error_data.get('error', 'Unknown error')}")
                    except:
                        print(f"Error details: {e.response.text}")
            except requests.exceptions.RequestException as e:
                print(f"Movie {movie_id} - Error connecting to server: {str(e)}")
                print("Make sure the server is running on http://127.0.0.1:8000")
        self.show_available_commands()

    def undo_last_watch(self, undo_token: str):
        """Remove last watched movie from history
        
        Args:
            undo_token: Token from server identifying the history entry
        """
        try:
            response = self.session.delete(
                f"{self.base_url}/history/{undo_token}"
            )
            response.raise_for_status()
            
            result = response.json()
            print(result.get('message', 'Last watch entry removed successfully!'))
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_history(self, arg):
        """View your watch history
        
        Usage: history
        """
        try:
            response = self.session.get(
                f"{self.base_url}/history/{self.current_user}"
            )
            response.raise_for_status()
            
            history = response.json()
            if not history:
                print("No watch history found.")
                self.show_available_commands()
                return
            
            print("\nWatch History:")
            print("-" * 50)
            for movie in history:
                print(f"Title: {movie['title']}")
                print(f"Watched on: {movie['watched_date'][:10]}")
                print("-" * 50)
            self.show_available_commands()
        except requests.exceptions.HTTPError as e:
            print(f"Server error: {e.response.status_code}")
            if e.response.text:
                try:
                    error_data = e.response.json()
                    print(f"Error details: {error_data.get('error', 'Unknown error')}")
                except:
                    print(f"Error details: {e.response.text}")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_genres(self, arg):
        """List all available genres
        
        Usage: genres
        """
        try:
            response = self.session.get(f"{self.base_url}/movies")
            response.raise_for_status()
            
            movies = response.json()
            genres = sorted(list(set(movie['genre'] for movie in movies)))
            
            print("\nAvailable Genres:")
            print("-" * 50)
            for genre in genres:
                print(f"- {genre}")
            print("-" * 50)
            print("\nTips:")
            print("- Use 'set preferences <genre1> <genre2> ...' to set your preferences")
            print("- Use 'remove preferences <genre1> <genre2> ...' to remove specific genre preferences")
            print("- Use 'preferences' to view movies in your preferred genres")
            self.show_available_commands()
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to server: {str(e)}")
            print("Make sure the server is running on http://127.0.0.1:8000")
            self.show_available_commands()

    def do_help(self, arg):
        """Show help about commands
        
        Usage: help [command]
        Example: help search
        """
        if arg:
            # Show help about a specific command
            super().do_help(arg)
        else:
            self.show_available_commands()

    def do_quit(self, arg):
        """Exit the program"""
        print("\nGoodbye!")
        return True

    def do_exit(self, arg):
        """Alias for quit"""
        return self.do_quit(arg)

    def default(self, line):
        """Handle unknown commands"""
        print(f"Unknown command: {line}")
        self.show_available_commands()

    def emptyline(self):
        """Show available commands on empty line to help users"""
        self.show_available_commands()

if __name__ == "__main__":
    try:
        MovieCLI().cmdloop()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
