# Movie Recommendation System

A microservices-based CLI for discovering, tracking, and getting personalized movie recommendations.

## Microservices Architecture

This system implements a microservices architecture with the following components:

1. **Main Program**: CLI-based movie search and recommendation interface
2. **Microservice A**: Movie Quotes Service
3. **Microservice B**: Recommendation Engine Service
4. **Microservice C**: Genre Analysis Service
5. **Microservice D**: Watch History Service

Each microservice runs as a separate process and communicates with the main program via REST APIs:
- Main Program: http://127.0.0.1:8000
- Microservice A (Movie Quotes): http://127.0.0.1:5004
- Microservice B (Recommendation): http://127.0.0.1:8001
- Microservice C (Genre Analysis): http://127.0.0.1:8002
- Microservice D (Watch History): http://127.0.0.1:8003

## Technologies Used

### Core Dependencies
- **Python 3.13.1** - Core programming language
- **Flask** - Web framework for server
- **Flask-CORS** - CORS support for Flask
- **Requests** - HTTP client for client.py
- **Werkzeug** - Required by Flask
- **Click** - Required by Flask

### CLI Interface
- **cmd** - Python library for CLI interface
- **colorama** - Terminal colors (Windows support, optional)

### Data Storage
- **JSON files** - Local data persistence
  - movies.json - Movie database
  - preferences.json - User preferences
  - history.json - Watch history

### Development Tools
- **VS Code** - Primary IDE
- **Git** - Version control
- **GitHub** - Repository hosting
- **venv** - Python virtual environment

### Code Quality
- **logging** - Debug and error logging
- **docstrings** - Function documentation

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Start the system:
```bash
python start.py
```
This will open two windows:
- Server window: Shows the server is running. Keep this window open.
- Client window: Interactive CLI for using the system.

## Using the CLI

Once you start the client, you'll see a welcome message and a prompt:
```
Welcome to the client Movie Recommendation System!
Track and discover movies you'll love.

⏱️  Quick commands - each takes <1 second to run
```

### Available Commands

At the `Command: ` prompt, you can use these commands:

1. **List All Movies**
```
Command: movies
```

2. **Search for Movies** (uses Microservice A)
```
Command: search "Dark Knight"
```

3. **View Available Genres**
```
Command: genres
```

4. **Set Genre Preferences**
```
Command: set preferences Action Sci-Fi
```
Note: Genre names are case-insensitive (e.g., 'action' = 'Action')

5. **Remove Genre Preferences**
```
Command: remove preferences Horror Comedy
```

6. **View Movies by Preferences**
```
Command: preferences
```

7. **Add Movies to Watch History**
```
Command: watch 1          # Add one movie
Command: watch 1 2 3      # Add multiple movies
```

8. **View Watch History**
```
Command: history
```

9. **Get Personalized Recommendations** (uses Microservice B)
```
Command: recommend
```

10. **View Genre Analysis** (uses Microservice C)
```
Command: analysis         # Detailed genre analysis
Command: popular          # Most popular genres
```

11. **View Watching Statistics** (uses Microservice D)
```
Command: stats            # Your watching statistics
Command: trends           # Overall watching trends
```

12. **Get Movie Quotes** (uses Microservice A)
```
Command: quote "Batman Begins"  # Get quote for a specific movie
Command: quote history          # View all queried quotes
Command: quote stats            # View genre popularity statistics
```

13. **Get Help**
```
Command: help             # List all commands
Command: help search      # Get help for specific command
```

13. **Exit the Program**
```
Command: quit
```
or
```
Command: exit
```

## Features

### User Stories
1. **Movie Search**
   - Search movies by title
   - View all available movies
   - See movie details (ID, title, genre, release date)

2. **Genre Management**
   - View all available genres
   - Set multiple genre preferences
   - Remove specific genre preferences
   - Case-insensitive genre matching

3. **Watch History**
   - Add single or multiple movies to history
   - View complete watch history with dates
   - Add movies directly from search results

### Inclusivity Features
1. **Value Communication**
   - Clear welcome message
   - Helpful command descriptions
   - Tips after each operation

2. **Cost Transparency**
   - Shows command execution time estimates
   - Clear setup requirements

3. **Content Control**
   - User-defined genre preferences
   - Customizable watch history
   - Multiple ways to add movies

4. **Familiar Patterns**
   - Standard CLI command patterns
   - Consistent command structure
   - Similar to popular CLIs

5. **Error Recovery**
   - Clear error messages
   - Recovery suggestions
   - Connection status checks

6. **Clear Next Steps**
   - Command tips after operations
   - Help menu with examples
   - Context-aware suggestions

7. **Multiple Pathways**
   - Full or partial title search
   - Multiple command formats
   - Case-insensitive matching

8. **Mistake Prevention**
   - Input validation
   - Command confirmation
   - Clear feedback

### Quality Attributes
1. **Maintainability**
   - Modular code structure
     - Server.py demonstrates clear separation of concerns:
       - Distinct functions for data operations (read_json_file, write_json_file)
       - Separate route handlers for each API endpoint
       - Modular error handling and logging
       - Clean configuration management
     - Client.py shows organized command structure:
       - Individual methods for each CLI command
       - Reusable error handling patterns
       - Consistent command parsing logic
   - Clear documentation
     - Comprehensive docstrings for all functions
     - Detailed API endpoint descriptions
     - Usage examples in command help text
   - Consistent formatting
     - Uniform indentation and spacing
     - Standard naming conventions
     - Regular code organization patterns
     - Predictable function structures

2. **Performance**
   - Quick command execution
   - Efficient data storage
   - Connection pooling

3. **Reliability**
   - Error handling
   - Data persistence
   - Server status checks

## For Teammates: Creating a Microservice

### 1. Clone and Setup
```bash
# Clone the repository
git clone https://github.com/xbenxspire/movie-recommendation-system.git
cd movie-recommendation-system

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # macOS/Linux

# Install dependencies
pip install -r requirements.txt
```

### 2. Test Main System
```bash
# Start the system
python start.py

# Try some commands in the client window:
Command: movies
Command: search "Dark Knight"
Command: help
```

### 3. Create Your Microservice
Choose one of these services to implement:

1. **Movie Rating Service**
   ```
   ratings> add <movie_id> <rating>    # Add rating (1-5)
   ratings> view <movie_id>            # View stats
   ratings> trending                   # Show trending
   ratings> compare <id1> <id2>        # Compare movies
   ```

2. **Similar Movies Service**
   ```
   similar> find <movie_id>            # Find similar
   similar> by-genre <genre1,genre2>   # Match genres
   similar> by-year <year> <range>     # Find in year range
   similar> by-plot <keywords>         # Find by plot
   ```

3. **Movie Quotes Service**
   ```
   quotes> add <movie_id> "<quote>"    # Add quote
   quotes> search "<text>"             # Search quotes
   quotes> random                      # Random quote
   quotes> by-movie <movie_id>         # Movie quotes
   ```

4. **Movie Reviews Service**
   ```
   reviews> add <movie_id> "<review>"  # Add review
   reviews> view <movie_id>            # View reviews
   reviews> search "<keyword>"         # Search reviews
   reviews> summary <movie_id>         # Get summary
   ```

### 4. Implementation Steps
1. Create your service files:
   ```
   microservices/
   └── your_service/
       ├── service.py      # Main service code
       ├── data.json       # Your service's data
       └── README.md       # Service documentation
   ```

2. Follow the main system's patterns:
   - Use cmd.Cmd for CLI interface
   - Store data in JSON files
   - Follow error handling patterns
   - Include help commands

3. Test your service:
   ```bash
   # Start your service
   python microservices/your_service/service.py
   ```

### 5. Integration
Your service should:
- Run independently like the main system
- Use JSON for data storage
- Follow the same CLI patterns
- Include clear error messages
- Provide help documentation

## Microservices Implementation

### Microservice B: Recommendation Engine Service
- **Purpose**: Processes user preferences and generates personalized movie recommendations
- **Endpoints**:
  - `/recommend` - Generate personalized recommendations based on user preferences
  - `/health` - Check service health
- **Features**:
  - Collaborative filtering based on preferences
  - Relevance scoring for recommendations
  - Explanation of recommendation reasons

### Microservice C: Genre Analysis Service
- **Purpose**: Categorizes movies and identifies genre patterns
- **Endpoints**:
  - `/genres` - List all genres with movie counts
  - `/genres/popular` - Get most popular genres
  - `/genres/analysis` - Get detailed genre analysis
  - `/genres/user/<user_id>` - Get genre analysis for specific user
  - `/health` - Check service health
- **Features**:
  - Genre distribution analysis
  - Decade-based genre trends
  - Popularity metrics

### Microservice D: Watch History Service
- **Purpose**: Tracks user viewing history and analyzes watching patterns
- **Endpoints**:
  - `/history/<user_id>` - Get user watch history
  - `/history/<user_id>/<movie_id>` - Add movie to history
  - `/history/stats/<user_id>` - Get user watching statistics
  - `/history/trends` - Get overall watching trends
  - `/health` - Check service health
- **Features**:
  - Watch history tracking
  - User-specific statistics
  - Overall trend analysis

## Files for Portfolio

### Core System Files
1. `client.py` - Interactive CLI interface
2. `server.py` - Backend server with REST API
3. `start.py` - Cross-platform startup script

### Microservices
1. `microservices/service_b.py` - Recommendation Engine Service
2. `microservices/service_c.py` - Genre Analysis Service
3. `microservices/service_d.py` - Watch History Service

### Data Files
1. `data/movies.json` - Movie database
2. `data/preferences.json` - User preferences storage
3. `data/history.json` - Watch history storage

### Documentation
1. `README.md` - System documentation and usage guide
2. `project_plan.md` - Project planning and architecture
3. `video_script.md` - Demo video script for Assignment 5
4. `video_script_assignment10.md` - Demo video script for Assignment 10

### Dependencies
1. `requirements.txt` - Python package dependencies

These files showcase:
- Clean code architecture (client/server separation)
- Data persistence (JSON storage)
