# Anime Recommendation System

## Overview

Welcome to the Anime Recommendation System! This project is designed to provide users with personalized anime recommendations based on their preferences. It leverages the AniList GraphQL API to fetch anime data and uses a REST API service for searching anime, managing user preferences, and providing personalized recommendations.

---

## Features

### 1. **Anime Search and Recommendation:**
- Search for anime by name or genre.
- Fetch recommended anime based on user preferences (e.g., favorite genres or watched anime).

### 2. **User Authentication:**
- User registration and login.
- JWT-based authentication for secure access to user-specific endpoints.

### 3. **User Preferences:**
- Users can manage their preferences, including favorite genres and watched anime.
- Recommendations are personalized based on user preferences.

### 4. **Database:**
- User data (credentials, preferences, watched anime, etc.) is stored in PostgreSQL.
- Anime data is fetched from the AniList GraphQL API.

---

## API Endpoints

- **POST /auth/register** – Register a new user.
- **POST /auth/login** – Login and retrieve a JWT token.
- **GET /anime/search** – Search anime by name or genre.
- **GET /anime/recommendations** – Fetch personalized recommendations for the authenticated user.
- **GET /auth/preferences** – Manage user preferences (e.g., favorite genres).

---

## Setup and Installation

### 1. **Clone the repository:**

```bash
git clone https://github.com/saraswatAnkit/Anime-Recommendation-System.git
cd Anime-Recommendation-System
