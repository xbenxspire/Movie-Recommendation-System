# Movie Recommendation System

A comprehensive movie recommendation system built with microservices architecture, providing personalized movie suggestions through an intuitive interface.

## Project Overview

This system helps users discover movies through:
- Personalized recommendations based on preferences
- Movie search and detailed information
- Watch history tracking
- Genre-based filtering

### Architecture

Built using microservices:

1. **Main Program**
   - Movie search and recommendation interface
   - User preference management
   - Recommendation results display
   - Watch history tracking

2. **Microservices**
   - Movie Information Service
   - Recommendation Engine Service
   - Genre Analysis Service
   - Watch History Service

### Technology Stack

- **Backend**: FastAPI
- **Database**: SQLAlchemy
- **API Communication**: HTTPX
- **Data Validation**: Pydantic
- **Testing**: Pytest
- **Code Quality**: Black formatter

## Features

- Text-based UI optimized for usability
- Local data storage with SQLAlchemy
- Async operations for quick responses
- Extensible architecture
- RESTful API communication
- Comprehensive error handling
- Data validation and transformation

## Development Setup

1. Install dependencies:
```bash
pip install poetry
poetry install
```

2. Install recommended VS Code extensions:
- Python (Microsoft)
- Python Test Explorer
- autoDocstring
- YAML
- Even Better TOML
- Black Formatter

3. Configure environment:
```bash
poetry add fastapi uvicorn jinja2 sqlalchemy httpx pytest black
```

## Project Structure

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

## Testing Strategy

- Unit tests for components
- Integration tests between services
- End-to-end testing
- Performance testing

## Contributing

This project is part of CS 361 at Oregon State University. Contributions are currently limited to course participants.

## License

[MIT License](LICENSE)
