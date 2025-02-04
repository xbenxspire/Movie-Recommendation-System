# Assignment 5 Video Script

## Introduction (0:00-0:15)
"Hi, I'm demonstrating my Movie Tracking System for CS361 Assignment 5. This CLI application showcases user stories, inclusivity heuristics, and quality attributes."

## System Overview (0:15-0:30)
"The system uses a client-server architecture with JSON data storage. Let me show you how to start it."
[Demo running start.bat]
"This opens both the server and client windows."

## User Stories (0:30-1:30)

### Movie Search (0:30-0:50)
"First user story: Movie search functionality. Watch how I can search for movies:"
```
movies> search "Dark Knight"
```
"Notice the detailed results including ID, title, genre, and release date."

### Genre Preferences (0:50-1:10)
"Second user story: Genre preference management. Users can set and update preferences:"
```
movies> set preferences Action Sci-Fi
movies> preferences
```
"The system shows movies matching these genres, with case-insensitive matching."

### Watch History (1:10-1:30)
"Third user story: Watch history tracking. Users can add movies and view their history:"
```
movies> watch 1 2 3
movies> history
```
"You can add multiple movies at once, and each entry includes the watch date."

## Inclusivity Heuristics (1:30-3:30)

### Value Communication (1:30-1:45)
"For value communication, notice the welcome message explaining benefits:"
[Show welcome message]
"It clearly states the system's purpose: tracking and discovering movies."

### Cost Transparency (1:45-2:00)
"For cost transparency, we show command timing estimates:"
[Point to '⏱️ Quick commands' message]
"Users know each command takes less than a second."

### Content Control (2:00-2:15)
"Users have full control over their content through preferences:"
```
movies> genres
movies> set preferences Action
movies> remove preferences Action
```

### Familiar Patterns (2:15-2:30)
"The CLI uses familiar command patterns:"
```
movies> help
movies> quit
```
"Similar to popular tools like git or npm."

### Error Recovery (2:30-2:45)
"For error handling, watch how it handles invalid genres:"
```
movies> set preferences InvalidGenre
```
"It shows valid options and explains case-insensitivity."

### Clear Next Steps (2:45-3:00)
"After each command, the system suggests next steps:"
[Show command tips]
"Making it easy to learn and use."

### Multiple Pathways (3:00-3:15)
"Users can accomplish tasks in multiple ways:"
```
movies> search Dark
movies> search "Dark Knight"
```
"Supporting different search styles."

### Mistake Prevention (3:15-3:30)
"The system prevents mistakes through validation:"
```
movies> watch abc
```
"Showing clear error messages and recovery steps."

## Quality Attributes (3:30-4:30)

### Maintainability (3:30-3:50)
"For maintainability, the code is modular and well-documented:"
[Show client.py and server.py structure]
"Each function has a single responsibility and clear documentation."

### Performance (3:50-4:10)
"For performance, commands execute quickly:"
[Demo rapid commands]
"Notice the sub-second response times for all operations."

### Reliability (4:10-4:30)
"For reliability, all errors are properly handled:"
[Demo error scenarios]
"The system remains stable and provides helpful feedback."

## Technical Features (4:30-4:45)
"Additional technical features include:"
- "Client-server architecture"
- "JSON data persistence"
- "RESTful API design"
- "Case-insensitive matching"

## Closing (4:45-5:00)
"This system demonstrates clean architecture, user-focused design, and robust error handling. Thank you for watching."

## Demo Preparation
1. Clear any existing data files
2. Start fresh server instance
3. Have example commands ready
4. Test error scenarios beforehand
5. Ensure clear terminal visibility
