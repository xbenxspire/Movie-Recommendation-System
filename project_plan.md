# CS 361 Project Plan

## Project Overview

This project will create a Movie Recommendation System using microservices:

**Main Program:**
- Movie search and recommendation interface
- User preference management
- Recommendation results display
- Watch history tracking

**Microservices:**
1. Movie Information Service (for teammate)
   - Movie details lookup
   - Cast and crew information
   - Release dates and ratings

2. Recommendation Engine Service
   - Processes user preferences
   - Generates personalized recommendations
   - Uses collaborative filtering

3. Genre Analysis Service
   - Categorizes movies
   - Identifies genre patterns
   - Provides genre-based suggestions

4. Watch History Service
   - Tracks user viewing history
   - Analyzes watching patterns
   - Suggests based on past behavior

**Key Features:**
- Text-based UI that's simple and works well
- Stores data locally with SQLAlchemy
- Quick responses with async operations
- Easy to add new features

**Portfolio Value:**
- Shows microservices design in action
- Shows data processing skills
- Highlights async Python knowledge
- Shows API design experience

## Technical Approach: Hybrid with Python

### Framework Analysis: Flask vs FastAPI

**Flask:**
- Lightweight and flexible web framework
- Large ecosystem and community support
- Simple to start with, gradual complexity
- Synchronous by default, but can be made async
- Great for traditional web applications
- More mature, with extensive documentation

**FastAPI:**
- Modern, high-performance framework
- Built for async operations by default
- Automatic API documentation (OpenAPI/Swagger)
- Type hints and data validation built-in
- Excellent for microservices architecture
- Better performance than Flask

**Recommendation: FastAPI**
- Better suited for microservices architecture
- Built-in async support crucial for service communication
- Automatic API documentation helps with team coordination
- Type validation reduces potential integration issues
- Modern features showcase advanced Python knowledge

### Technology Stack

**Main Program:**
- FastAPI for backend API
- Python 3.13.1 (already installed)
- Jinja2 templates for server-side rendering
- Optional: Simple JavaScript for frontend interactivity
- SQLAlchemy for any data persistence needs

**Microservices:**
- FastAPI for Python-based services
- Pydantic for data validation
- HTTPX for async HTTP calls
- Docker for containerization (optional)
- Can integrate with teammate's services regardless of their stack

**Development Environment:**
- VS Code
- Poetry for dependency management
- Pytest for testing
- Black for code formatting
- Uvicorn as ASGI server

**VS Code Extensions:**
- "Python" by Microsoft (includes Pylance)
- "Python Test Explorer for Visual Studio Code" by Little Fox Team
- "autoDocstring - Python Docstring Generator" by Nils Werner
- "YAML" by Red Hat
- "Even Better TOML" by tamasfe (for Poetry's pyproject.toml)
- "Black Formatter" by Microsoft (for Python formatting)

## Project Timeline

### Sprint 1 (Weeks 2-3)
- [x] Complete project plan
- [x] Design user interface with inclusivity in mind
- [x] Create basic main program structure
- [x] Set up development environment
- [x] Plan microservice work with teammate

### Sprint 2 (Weeks 4-5) 
- [x] Build microservice for teammate
- [x] Write microservice API docs
- [x] Test microservice connections
- [x] Plan personal microservices

### Sprint 3 (Weeks 6-8)
- [ ] Build 3 microservices for main program
- [ ] Connect teammate's microservice
- [ ] Test everything works together
- [ ] Get project ready to show

### Final Week
- [ ] Test everything works
- [ ] Finish documentation
- [ ] Prepare presentation

### Assignment 5 Achievements
1. **User Stories Implementation**
   - Movie search functionality
   - Genre preference management
   - Watch history tracking

2. **Inclusivity Heuristics**
   - Value communication through clear messages
   - Cost transparency with timing estimates
   - Content control via preferences
   - Familiar CLI patterns
   - Error recovery with helpful messages
   - Clear next steps after commands
   - Multiple pathways for tasks
   - Mistake prevention with validation

3. **Quality Attributes**
   - Maintainability through modular design
   - Performance with quick responses
   - Reliability with error handling

## Microservices Architecture

### Main Program
- Web-based user interface
- Responsive design for multiple devices
- Modern frontend framework integration
- RESTful API communication
- Error handling with user feedback
- Data validation and transformation

### Microservices Design
1. Service A (For Teammate)
   - Single responsibility principle
   - Clear API documentation
   - Error handling
   - Input validation

2. Services B, C, D (For Main Program)
   - Independent, focused functionality
   - Standardized communication protocol
   - Strong error handling
   - Performance optimization

## Communication Protocol

- RESTful API endpoints using FastAPI
- Automatic OpenAPI/Swagger documentation
- JSON data format with Pydantic validation
- Async communication between services
- Type-safe request/response models
- Standardized error responses
- Health check endpoints with FastAPI dependencies

**CORS Configuration:**
```python
# FastAPI CORS setup in each service
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
- Development: Allow all origins for easy testing
- Production: Restrict to specific service origins
- Middleware configuration in each microservice
- Built-in FastAPI CORS support (no extra packages needed)

## Testing Strategy

- Unit tests for each component
- Integration tests between services
- End-to-end testing scenarios
- Performance and load testing

## Risk Management

### Potential Risks
1. Server availability and uptime
2. API compatibility between services
3. CORS and security concerns
4. Cloud hosting costs
5. Integration challenges with teammate's code
6. Performance bottlenecks
7. Scope creep
8. Video presentation quality
9. Service communication failures

### Mitigation Strategies
1. Use cloud platforms with free options
2. Write clear API docs and version control
3. Set up CORS in FastAPI correctly
4. Watch cloud usage costs
5. Keep in touch with teammate
6. Watch and fix performance issues
7. Keep project focused
8. Record voiceovers separately
9. Add backup plans for errors

## Success Criteria

1. Main program works with all microservices
2. Makes things easy for all users
3. Teammate can use our service
4. Each part runs on its own
5. Handles errors well
6. Good docs and demo materials

## Teammate Microservice Ideas

### 1. Movie Rating Service (CLI)
- **Purpose:** Aggregate and analyze movie ratings
- **Features:**
  - Calculate average ratings from user inputs
  - Track rating trends over time
  - Generate rating statistics
- **Commands:**
  ```
  ratings> add <movie_id> <rating>    # Add a rating (1-5)
  ratings> view <movie_id>            # View ratings stats
  ratings> trending                   # Show trending movies
  ratings> compare <id1> <id2>        # Compare two movies
  ```
- **Easy Implementation:** Store ratings in JSON, simple stats calculations

### 2. Similar Movies Service (CLI)
- **Purpose:** Find movie recommendations based on similarities
- **Features:**
  - Match movies by genre combinations
  - Find movies with similar release years
  - Suggest based on plot keywords
- **Commands:**
  ```
  similar> find <movie_id>            # Find similar movies
  similar> by-genre <genre1,genre2>   # Find by genres
  similar> by-year <year> <range>     # Find in year range
  similar> by-plot <keywords>         # Find by plot words
  ```
- **Easy Implementation:** Use movie metadata JSON for matching

### 3. Movie Quotes Service (CLI)
- **Purpose:** Manage and search movie quotes
- **Features:**
  - Store and retrieve famous quotes
  - Search by movie or character
  - Random quote generator
- **Commands:**
  ```
  quotes> add <movie_id> "<quote>"    # Add new quote
  quotes> search "<text>"             # Search quotes
  quotes> random                      # Get random quote
  quotes> by-movie <movie_id>         # Get movie quotes
  ```
- **Easy Implementation:** Store quotes in JSON database

### 4. Movie Reviews Service (CLI)
- **Purpose:** Manage text-based movie reviews
- **Features:**
  - Add and view user reviews
  - Search reviews by keyword
  - Generate review summaries
- **Commands:**
  ```
  reviews> add <movie_id> "<review>"  # Add review
  reviews> view <movie_id>            # View reviews
  reviews> search "<keyword>"         # Search reviews
  reviews> summary <movie_id>         # Get review summary
  ```
- **Easy Implementation:** Store reviews in JSON, text analysis

Each service:
- Uses simple CLI interface like main program
- Stores data in JSON files
- Includes error handling
- Provides help commands
- Has clear documentation
- Easy to test with example data

## Next Steps

1. Share microservice ideas with teammates
2. Set up development environment:
   - Install Poetry: `pip install poetry`
   - Configure VS Code settings for Python 3.13.1
   - Install recommended VS Code extensions
   - Set up FastAPI and dependencies via Poetry:
     ```
     poetry new project
     cd project
     poetry add fastapi uvicorn jinja2 sqlalchemy httpx pytest black
     ```
3. Create project structure:
   ```
   project/
   ├── main_program/
   │   ├── app/
   │   │   ├── __init__.py
   │   │   ├── main.py
   │   │   ├── api/
   │   │   ├── models/
   │   │   └── templates/
   │   ├── tests/
   │   └── pyproject.toml
   ├── microservices/
   │   ├── service_a/  # For teammate
   │   ├── service_b/
   │   ├── service_c/
   │   └── service_d/
   └── docs/
   ```
4. Start UI design with inclusivity focus
5. Coordinate microservice requirements
6. Begin FastAPI implementation
