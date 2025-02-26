# Project Brief: Movie Recommendation System

## Project Overview

The Movie Recommendation System is a microservices-based CLI application that helps users discover, track, and receive personalized movie recommendations. The system is designed for CS 361 at Oregon State University as part of a collaborative project demonstrating microservices architecture.

## Core Requirements

1. **Main Program**: A CLI-based interface for users to interact with the movie recommendation system
2. **Microservices Architecture**: Implementation of multiple microservices that run as separate processes
3. **Programmatic Communication**: Communication between the Main Program and microservices without direct function calls
4. **Data Persistence**: Storage of movie data, user preferences, and watch history

## Microservices

1. **Microservice A** (from teammate): Movie Information Service
   - Provides detailed movie information including cast, crew, release dates, and ratings

2. **Microservice B**: Recommendation Engine Service
   - Processes user preferences and generates personalized movie recommendations
   - Uses collaborative filtering and relevance scoring

3. **Microservice C**: Genre Analysis Service
   - Categorizes movies and identifies genre patterns
   - Provides genre distribution analysis and trends

4. **Microservice D**: Watch History Service
   - Tracks user viewing history and analyzes watching patterns
   - Provides statistics and trend analysis

## Technical Stack

- **Language**: Python 3.13.1
- **Web Framework**: Flask
- **CLI Interface**: cmd module
- **Data Storage**: JSON files
- **Communication**: REST APIs

## Project Goals

1. Demonstrate a working microservices architecture
2. Provide a useful movie recommendation experience
3. Implement inclusivity features for better user experience
4. Ensure maintainability, performance, and reliability
5. Create a demo video showcasing the system's features and architecture

## Timeline

This project is part of CS 361 Assignment 10, which requires creating a demo video showcasing the features of the implementation and its integrations with Microservices A, B, C, and D.

## Success Criteria

1. All microservices run in separate processes
2. Main Program communicates with microservices programmatically
3. System provides personalized movie recommendations
4. Users can track their watch history and preferences
5. Demo video clearly demonstrates the system's features and architecture
