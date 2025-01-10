# CS361: Assignment 2 - Environment Setup, Course Project Plan, and Sprint 1 Plan

## Part 1: Environment Setup

### 1. GitHub Repository

a) GitHub username: xbenxspire

b) Screenshot of test commit:
[Screenshot placeholder]

### 2. Spike: Task Management Systems

a) Task management systems evaluated:
- Trello
- Jira
- Asana

b) Screenshots of "CS361 Test Task" in each system:
[Screenshots placeholder]

c) Evaluation of each system:

**Ease of use:**

Trello:
Trello offers an intuitive drag-and-drop interface that's immediately understandable. The Kanban board layout makes it easy to visualize task flow, and the learning curve is minimal with helpful tooltips and guides.

Jira:
Jira has a steeper learning curve with its extensive feature set. While it offers comprehensive project management tools, the interface can be overwhelming for new users and requires time to learn all the available features.

Asana:
Asana provides a clean, modern interface that balances functionality with simplicity. The platform offers multiple view options (list, board, timeline) and includes helpful onboarding tutorials.

**Speed/responsiveness:**

Trello:
Trello loads quickly and updates in real-time. Card movements and updates are instantaneous, and the interface remains responsive even with multiple boards and cards.

Jira:
Jira can be slower to load initially and when switching between different views. The robust feature set sometimes impacts performance, especially when dealing with large projects.

Asana:
Asana maintains good performance with quick loading times. The interface updates smoothly, though some features like timeline views can take longer to load with many tasks.

**Feature set:**

Trello:
Trello offers essential task management features with a focus on simplicity. The Power-Up system allows adding specific features as needed, though some advanced project management features require paid plans.

Jira:
Jira provides the most comprehensive feature set, including advanced agile tools, detailed reporting, and extensive customization options. It's particularly strong for software development projects.

Asana:
Asana balances features well, offering task dependencies, custom fields, and multiple project views. It includes team collaboration features and workflow automation tools.

**Relevance/popularity:**

Trello:
Trello is widely used across various industries and is particularly popular in startups and small teams. Its simplicity makes it relevant for both personal and professional use.

Jira:
Jira is the industry standard for software development teams and is used by many major tech companies. Experience with Jira is highly valuable for software engineering careers.

Asana:
Asana has growing adoption in professional settings, especially among marketing and creative teams. It's becoming increasingly relevant in tech companies for non-engineering teams.

d) Rankings:

Trello:
- Ease of use: 1st
- Speed/responsiveness: 1st
- Feature set: 3rd
- Relevance/popularity: 2nd

Jira:
- Ease of use: 3rd
- Speed/responsiveness: 3rd
- Feature set: 1st
- Relevance/popularity: 1st

Asana:
- Ease of use: 2nd
- Speed/responsiveness: 2nd
- Feature set: 2nd
- Relevance/popularity: 3rd

e) Highest ranked system: Jira
While Trello wins in ease of use and speed, Jira's superior feature set and industry relevance make it the best choice for a software engineering project. Its comprehensive agile tools and integration capabilities will be valuable for managing the microservices architecture project.

## Part 2: Course Project Plan

### 1. Product Goal and Backlog

a) Product Goal:
Develop a comprehensive movie recommendation system that helps users discover personalized movie suggestions through an intuitive interface, leveraging microservices architecture to provide real-time recommendations based on user preferences, viewing history, and genre analysis.

b) User Stories:

1. Search Movies
- As a movie enthusiast, I want to search for movies by title so that I can quickly find specific films I'm interested in.

2. View Movie Details
- As a user, I want to view detailed information about a movie so that I can learn more about its plot, cast, and ratings.

3. Rate Movies
- As a user, I want to rate movies I've watched so that I can keep track of my opinions and improve future recommendations.

4. Get Recommendations
- As a user, I want to receive personalized movie recommendations so that I can discover new films that match my interests.

5. Create Watchlist
- As a user, I want to save movies to a watchlist so that I can keep track of films I want to watch later.

6. Filter Recommendations
- As a user, I want to filter movie recommendations by genre so that I can find specific types of movies I'm in the mood for.

7. View Watch History
- As a user, I want to view my watch history so that I can remember what movies I've already seen.

8. Share Recommendations
- As a user, I want to share movie recommendations with friends so that we can discuss films we might enjoy together.

9. Set Preferences
- As a user, I want to set my genre preferences so that I receive more relevant movie recommendations.

10. Get Similar Movies
- As a user, I want to see similar movies to ones I've enjoyed so that I can find more content I might like.

[Screenshot of user stories in task management system placeholder]

### 2. Quality Attributes

a) Selected quality attributes:

1. Usability
- Definition: The degree to which the system can be easily used by its intended users to achieve their goals effectively and efficiently.

2. Performance
- Definition: The speed and efficiency with which the system responds to user actions and processes data.

3. Reliability
- Definition: The ability of the system to perform its required functions consistently and accurately under normal conditions.

b) Relevance to project:

- Usability is crucial for this project as users need to easily search for movies and understand recommendations without confusion or frustration. The interface must be intuitive for users of varying technical abilities.

- Performance is essential because users expect quick responses when searching for movies and receiving recommendations. Slow loading times or delayed updates would significantly impact user satisfaction.

- Reliability is vital because users depend on accurate movie recommendations and consistent system behavior. The system must maintain data integrity and provide dependable service to build user trust.

## Part 3: Sprint 1 Plan

1. Sprint Goal:
Implement the core movie search and basic recommendation functionality, focusing on creating a usable and responsive user interface that allows users to search for movies, view details, and receive initial recommendations.

2. Sprint Backlog User Stories:

First user story:
(Front of index card)
Search Movies

As a movie enthusiast, I want to search for movies by title so that I can quickly find specific films I'm interested in.

(Back of index card)
Acceptance criteria

Functional requirements:
- Given the user is on the main page when they enter a movie title in the search bar and press enter, then a list of matching movies should be displayed.

Quality attributes & Non-functional requirements:
- Performance: Search results must be displayed within 2 seconds of submitting the search query.

Second user story:
(Front of index card)
View Movie Details

As a user, I want to view detailed information about a movie so that I can learn more about its plot, cast, and ratings.

(Back of index card)
Acceptance criteria

Functional requirements:
- Given a user has searched for movies when they click on a movie title then the detailed information page for that movie should be displayed.

Quality attributes & Non-functional requirements:
- Usability: Movie details must be organized in clear sections with consistent formatting and readable text size.

Third user story:
(Front of index card)
Get Recommendations

As a user, I want to receive personalized movie recommendations so that I can discover new films that match my interests.

(Back of index card)
Acceptance criteria

Functional requirements:
- Given a user has viewed at least one movie when they visit the recommendations page then a list of recommended movies based on their viewing history should be displayed.

Quality attributes & Non-functional requirements:
- Reliability: The recommendation system must maintain 99% uptime during operating hours and provide consistent recommendations for the same user profile.

[Screenshot of Sprint Backlog in task management system placeholder]
