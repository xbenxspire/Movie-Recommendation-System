# Technical Context: Movie Recommendation System

## Technologies Used

### Core Technologies

1. **Python 3.13.1**
   - Primary programming language
   - Features used: type hints, f-strings, context managers
   - Standard library modules: cmd, json, datetime, logging, os, sys

2. **Flask 2.0+**
   - Web framework for RESTful APIs
   - Used for all server components
   - Features: route decorators, JSON responses, error handling
   - Extensions: Flask-CORS for cross-origin resource sharing

3. **Requests**
   - HTTP client library
   - Used for inter-service communication
   - Features: session management, JSON handling, error handling

4. **JSON**
   - Data interchange format
   - Used for API responses and data storage
   - Native Python support via json module

### Supporting Technologies

1. **cmd Module**
   - Command-line interface framework
   - Provides command parsing and help system
   - Used for the client interface

2. **subprocess Module**
   - Process management
   - Used to start components as separate processes
   - Platform-independent process creation

3. **logging Module**
   - Structured logging
   - Used for debugging and error tracking
   - Configurable output formats and destinations

4. **Werkzeug**
   - WSGI utility library
   - Required by Flask
   - Provides HTTP utilities and debugging tools

5. **Click**
   - Command-line interface creation toolkit
   - Required by Flask
   - Used for Flask CLI commands

## Development Setup

### Environment Setup

1. **Python Installation**
   - Python 3.13.1 or higher
   - pip package manager
   - venv module for virtual environments

2. **Virtual Environment**
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Dependencies Installation**
   ```bash
   # Install dependencies
   pip install -r requirements.txt
   ```

### Project Structure

```
movie-recommendation-system/
├── client.py              # CLI interface
├── server.py              # Main server
├── start.py               # Startup script
├── requirements.txt       # Dependencies
├── README.md              # Documentation
├── data/
│   ├── movies.json        # Movie database
│   ├── preferences.json   # User preferences
│   └── history.json       # Watch history
├── microservices/
│   ├── service_b.py       # Recommendation Engine
│   ├── service_c.py       # Genre Analysis
│   └── service_d.py       # Watch History
└── memory-bank/           # Project documentation
```

### Running the System

1. **Start All Components**
   ```bash
   python start.py
   ```
   This will:
   - Start the main server on port 8000
   - Start Microservice B on port 8001
   - Start Microservice C on port 8002
   - Start Microservice D on port 8003
   - Start the client CLI

2. **Manual Component Startup**
   ```bash
   # Start main server
   python server.py
   
   # Start microservices
   python microservices/service_b.py
   python microservices/service_c.py
   python microservices/service_d.py
   
   # Start client
   python client.py
   ```

## Technical Constraints

### Performance Constraints

1. **Response Time**
   - All commands should execute in under 1 second
   - Microservices should respond within 500ms
   - Data loading should be efficient for large datasets

2. **Memory Usage**
   - System should work with limited memory (< 512MB)
   - No memory leaks in long-running processes
   - Efficient data structures for in-memory operations

3. **Startup Time**
   - System should start up in under 5 seconds
   - Microservices should initialize quickly
   - Client should connect promptly

### Compatibility Constraints

1. **Python Version**
   - Minimum: Python 3.8
   - Recommended: Python 3.13.1
   - No dependencies on deprecated features

2. **Operating Systems**
   - Windows 10/11
   - macOS 10.15+
   - Linux (Ubuntu 20.04+)
   - Cross-platform compatibility for all components

3. **Terminal Compatibility**
   - Standard terminal emulators
   - Windows Command Prompt and PowerShell
   - Support for basic terminal features (colors, input)

### Security Constraints

1. **Data Privacy**
   - User data stored locally only
   - No external API calls
   - No collection of personal information

2. **Input Validation**
   - All user input validated before processing
   - Protection against injection attacks
   - Secure handling of file operations

3. **Error Handling**
   - No exposure of sensitive information in errors
   - Graceful handling of unexpected inputs
   - Proper logging of security-related events

## Dependencies

### Core Dependencies

1. **Flask**
   - Version: 2.0.0+
   - Purpose: Web framework for RESTful APIs
   - Website: https://flask.palletsprojects.com/

2. **Flask-CORS**
   - Version: 3.0.0+
   - Purpose: Cross-Origin Resource Sharing support
   - Website: https://flask-cors.readthedocs.io/

3. **Requests**
   - Version: 2.25.0+
   - Purpose: HTTP client for API communication
   - Website: https://docs.python-requests.org/

### Indirect Dependencies

1. **Werkzeug**
   - Version: 2.0.0+
   - Purpose: WSGI utility library (required by Flask)
   - Website: https://werkzeug.palletsprojects.com/

2. **Click**
   - Version: 8.0.0+
   - Purpose: Command-line interface toolkit (required by Flask)
   - Website: https://click.palletsprojects.com/

3. **MarkupSafe**
   - Version: 2.0.0+
   - Purpose: String handling (required by Flask)
   - Website: https://markupsafe.palletsprojects.com/

4. **Jinja2**
   - Version: 3.0.0+
   - Purpose: Template engine (required by Flask)
   - Website: https://jinja.palletsprojects.com/

5. **itsdangerous**
   - Version: 2.0.0+
   - Purpose: Data signing (required by Flask)
   - Website: https://itsdangerous.palletsprojects.com/

### Development Dependencies

1. **pytest**
   - Version: 6.0.0+
   - Purpose: Testing framework
   - Website: https://docs.pytest.org/

2. **flake8**
   - Version: 3.9.0+
   - Purpose: Code linting
   - Website: https://flake8.pycqa.org/

3. **black**
   - Version: 21.5b2+
   - Purpose: Code formatting
   - Website: https://black.readthedocs.io/

## API Documentation

### Main Server API

1. **GET /movies**
   - Purpose: List all available movies
   - Response: Array of movie objects
   - Status codes: 200 (Success), 500 (Server Error)

2. **GET /movies/search/{query}**
   - Purpose: Search movies by title
   - Parameters: query (string)
   - Response: Array of matching movie objects
   - Status codes: 200 (Success), 500 (Server Error)

3. **GET /preferences/{user_id}**
   - Purpose: Get user preferences
   - Parameters: user_id (integer)
   - Response: Object with preferred_genres array
   - Status codes: 200 (Success), 500 (Server Error)

4. **POST /preferences/{user_id}**
   - Purpose: Set user preferences
   - Parameters: user_id (integer)
   - Request body: { "preferred_genres": ["Action", "Sci-Fi"] }
   - Response: Success message
   - Status codes: 200 (Success), 400 (Bad Request), 500 (Server Error)

5. **GET /history/{user_id}**
   - Purpose: Get user watch history
   - Parameters: user_id (integer)
   - Response: Array of watched movie objects with dates
   - Status codes: 200 (Success), 500 (Server Error)

6. **POST /history/{user_id}/{movie_id}**
   - Purpose: Add movie to watch history
   - Parameters: user_id (integer), movie_id (integer)
   - Response: Success message
   - Status codes: 200 (Success), 404 (Not Found), 500 (Server Error)

7. **DELETE /history/{undo_token}**
   - Purpose: Remove last watched movie
   - Parameters: undo_token (string)
   - Response: Success message
   - Status codes: 200 (Success), 404 (Not Found), 500 (Server Error)

### Microservice B API

1. **POST /recommend**
   - Purpose: Get personalized recommendations
   - Request body: { "user_id": 1, "preferred_genres": ["Action", "Sci-Fi"] }
   - Response: Object with recommendations array
   - Status codes: 200 (Success), 400 (Bad Request), 500 (Server Error)

2. **GET /health**
   - Purpose: Check service health
   - Response: Status and timestamp
   - Status codes: 200 (Success)

### Microservice C API

1. **GET /genres**
   - Purpose: List all genres with counts
   - Response: Object with genres array
   - Status codes: 200 (Success), 500 (Server Error)

2. **GET /genres/popular**
   - Purpose: Get most popular genres
   - Response: Object with popular_genres array
   - Status codes: 200 (Success), 500 (Server Error)

3. **GET /genres/analysis**
   - Purpose: Get detailed genre analysis
   - Response: Object with genres and decades arrays
   - Status codes: 200 (Success), 500 (Server Error)

4. **GET /genres/user/{user_id}**
   - Purpose: Get genre analysis for user
   - Parameters: user_id (integer)
   - Response: Object with genre breakdown
   - Status codes: 200 (Success), 500 (Server Error)

5. **GET /health**
   - Purpose: Check service health
   - Response: Status and timestamp
   - Status codes: 200 (Success)

### Microservice D API

1. **GET /history/{user_id}**
   - Purpose: Get user watch history
   - Parameters: user_id (integer)
   - Response: Object with history array
   - Status codes: 200 (Success), 500 (Server Error)

2. **POST /history/{user_id}/{movie_id}**
   - Purpose: Add movie to watch history
   - Parameters: user_id (integer), movie_id (integer)
   - Response: Success message
   - Status codes: 200 (Success), 404 (Not Found), 500 (Server Error)

3. **GET /history/stats/{user_id}**
   - Purpose: Get user watching statistics
   - Parameters: user_id (integer)
   - Response: Object with statistics
   - Status codes: 200 (Success), 500 (Server Error)

4. **GET /history/trends**
   - Purpose: Get overall watching trends
   - Response: Object with trends data
   - Status codes: 200 (Success), 500 (Server Error)

5. **GET /health**
   - Purpose: Check service health
   - Response: Status and timestamp
   - Status codes: 200 (Success)
