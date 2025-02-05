# Assignment 5 Video Script

## Introduction (0:00-0:15)
"Hi, I'm demonstrating my Movie Recommendation System for CS361 Assignment 5. Let me show you how it satisfies the requirements through user stories, inclusivity heuristics, and quality attributes."

## User Stories (0:15-1:00)

### Movie Search (0:15-0:30)
"For my first user story: As a movie fan, I want to search for movies by title so that I can find specific films I'm interested in. Given the user is at the movies prompt, when they search for 'Dark Knight', then they see the movie details including ID, title, genre, and release date."
```
Command: search "Dark Knight"
```

### Genre Management (0:30-0:45)
"For my second user story: As a user, I want to set my genre preferences so that I can focus on movies I enjoy. Given the user knows their preferred genres, when they set preferences to Action and Sci-Fi, then they see only movies from those genres."
```
Command: set preferences Action Sci-Fi
Command: preferences
```

### Watch History (0:45-1:00)
"For my third user story: As a movie viewer, I want to track my watch history so that I can remember what I've watched. Given the user has found movies they like, when they add movies to their history, then they can view their complete watch history with dates."
```
Command: watch 1 2 3
Command: history
```

## Inclusivity Heuristics (1:00-3:00)

### Value Communication (1:00-1:15)
"For Inclusivity Heuristic #1: Here's the welcome message explaining the value: 'Discover and get personalized movie recommendations you'll love.'"

### Cost Transparency (1:15-1:30)
"For Inclusivity Heuristic #2: Here we show command timing estimates with '⏱️ Quick commands - each takes <1 second to run'"

### Content Control (1:30-1:45)
"For Inclusivity Heuristic #3: Users can control their content by setting and removing genre preferences:"
```
Command: set preferences Action
Command: remove preferences Action
```

### Familiar Patterns (1:45-2:00)
"For Inclusivity Heuristic #4: The CLI uses familiar command patterns like help and quit, similar to git or npm."

### Error Recovery (2:00-2:15)
"For Inclusivity Heuristic #5: Users can recover from errors. Watch how it handles invalid input:"
```
Command: set preferences InvalidGenre
```

### Clear Next Steps (2:15-2:30)
"For Inclusivity Heuristic #6: After each command, the system suggests next steps."
[Show command tips]

### Multiple Pathways (2:30-2:45)
"For Inclusivity Heuristic #7: Users can accomplish tasks in multiple ways:"
```
Command: search Dark
Command: search "Dark Knight"
```

### Mistake Prevention (2:45-3:00)
"For Inclusivity Heuristic #8: The system prevents mistakes through validation:"
```
Command: watch abc
```

## Quality Attributes (3:00-3:45)

### Maintainability (3:00-3:15)
"For maintainability: The non-functional requirement is 'Code must have modular structure and consistent formatting.' As you can see in server.py and client.py, functions are organized by responsibility with consistent documentation and formatting patterns."

### Performance (3:15-3:30)
"For performance: The non-functional requirement is 'Commands must execute in under 1 second.' Watch these rapid commands execute instantly:"
[Demo rapid commands]

### Reliability (3:30-3:45)
"For reliability: The non-functional requirement is 'All errors must be handled gracefully.' Watch how the system handles various error scenarios while remaining stable:"
[Demo error scenarios]

## Closing (3:45-4:00)
"This system demonstrates working functionality that provides real value to users through an inclusive, maintainable, and reliable design. Thank you for watching."

## Demo Preparation
1. Reset user data while keeping movies list:
   ```
   # Delete user data files (preferences and history)
   del data/preferences.json
   del data/history.json
   
   # Server will automatically recreate these as empty files
   ```
2. Start fresh server instance:
   ```
   python start.py
   ```
3. Have these commands ready in order:
   - search "Dark Knight"
   - set preferences Action Sci-Fi
   - preferences
   - watch 1 2 3
   - history
   - set preferences InvalidGenre
   - search Dark
   - watch abc
4. Test error scenarios beforehand
5. Ensure clear terminal visibility
   - Use a dark theme if possible
   - Maximize terminal window
   - Clear terminal before recording (cls command)
