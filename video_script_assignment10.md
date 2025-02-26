# Assignment 10 Video Script: Microservices Implementation

## Introduction (0:00-0:30)

"Hello, I'm demonstrating my Movie Recommendation System for CS361 Assignment 10. This system provides value to users by helping them discover movies they'll enjoy based on their preferences, viewing history, and genre interests. It saves users time by offering personalized recommendations without requiring them to search through large movie catalogs."

## Main Features and Microservices (0:30-2:30)

### Feature 1: Movie Quotes (Microservice A) (0:30-0:55)

"First, let me show you the movie quotes feature. This functionality uses Microservice A, implemented by my teammate, which provides famous quotes from movies along with details about who said them and in what context."

[SHOW: Quote functionality and results from Microservice A]
```
Command: quote "Batman Begins"
Command: quote history
Command: quote stats
```

"As you can see, Microservice A returns quotes from the specified movie, along with information about the character who said it, the genre, and context. It also tracks quote history and provides genre statistics for the quotes you've looked up."

### Feature 2: Personalized Recommendations (Microservice B) (0:55-1:20)

"Next, users can get personalized movie recommendations based on their preferences. This feature uses Microservice B, our Recommendation Engine Service, which processes user preferences and generates tailored suggestions."

[SHOW: Setting preferences and getting recommendations]
```
Command: set preferences Action Sci-Fi
Command: recommend
```

"Microservice B analyzes user preferences and provides personalized recommendations with relevance scores and explanations."

### Feature 3: Genre Analysis (Microservice C) (1:20-1:45)

"Users can also explore movies by genre and discover genre patterns. This functionality is provided by Microservice C, our Genre Analysis Service, which categorizes movies and identifies genre trends."

[SHOW: Genre analysis features]
```
Command: analysis
Command: popular
```

"Microservice C provides detailed genre analysis, including distribution across decades and popularity metrics."

### Feature 4: Watch History (Microservice D) (1:45-2:10)

"Finally, the system tracks viewing history and provides statistics based on watching patterns. This is handled by Microservice D, our Watch History Service."

[SHOW: Adding movies to history and viewing statistics]
```
Command: watch 1 7 9
Command: history
Command: stats
Command: trends
```

"Microservice D tracks what users watch and analyzes patterns to provide insights into viewing habits."

### Integration Overview (2:10-2:30)

"These four microservices work together to provide a comprehensive movie recommendation experience. Each handles a specific aspect of the system's functionality, communicating with the main program through well-defined interfaces."

## Separate Processes Demonstration (2:30-3:00)

"Now, let me show you that the Main Program and each microservice run in separate processes. Here I'm showing all five components running independently."

[SHOW: Terminal windows or Task Manager showing separate processes]

"As you can see, we have:
1. The Main Program running on port 8000
2. Microservice A (from my teammate) running as a separate process
3. Microservice B (Recommendation Engine) running on port 8001
4. Microservice C (Genre Analysis) running on port 8002
5. Microservice D (Watch History) running on port 8003

Each component runs in its own process, allowing for independent development, deployment, and scaling."

## Communication Demonstration (3:00-3:30)

"The Main Program communicates with each microservice programmatically without direct function calls. Let me show you the code that demonstrates this communication."

[SHOW: Code snippets from client.py showing API calls to microservices]

"Here you can see that the Main Program makes HTTP requests to each microservice. For example, when getting recommendations, it sends a POST request to Microservice B's endpoint with user preferences as JSON data. The microservice processes this request and returns recommendations, which the Main Program then displays to the user.

There are no direct imports or function calls between the Main Program and the microservices - all communication happens through well-defined APIs."

## Conclusion (3:30-3:45)

"This completes the demonstration of our Movie Recommendation System and its integrated microservices. The system demonstrates the power of microservices architecture, where each component has a single responsibility and communicates through well-defined interfaces. This approach allows for independent development, testing, and deployment of each component, making the system more maintainable and scalable."

## Demo Preparation

1. Start all components:
   ```
   python start.py
   ```
   
2. Have these commands ready in order:
   - quote "Batman Begins"
   - quote history
   - quote stats
   - set preferences Action Sci-Fi
   - recommend
   - analysis
   - popular
   - watch 1 7 9
   - history
   - stats
   - trends

3. Prepare to show:
   - All processes running (Task Manager or terminal windows)
   - Code snippets showing communication between Main Program and microservices

4. Ensure clear terminal visibility:
   - Use a dark theme if possible
   - Maximize terminal windows
   - Clear terminal before recording (cls command)
