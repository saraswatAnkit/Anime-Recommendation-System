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

```

##2. Create and activate a virtual environment:
python -m venv env
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate
##3. Install the dependencies:
pip install -r requirements.txt
##4. Set up environment variables:
Create a .env file in the root directory of your project with the following values:

DATABASE_URL=your_postgresql_database_url
SECRET_KEY=your_secret_key
DEBUG=True
Replace the values of DATABASE_URL and SECRET_KEY with your actual credentials.

##5. Apply database migrations:
python manage.py migrate
6. Run the server:
python manage.py runserver
The application should now be running on http://127.0.0.1:8000/.

Database
This project uses PostgreSQL as the database for storing user data and preferences. Ensure that you have PostgreSQL installed and set up a database with proper credentials.

You can configure your database connection string in the .env file as DATABASE_URL=your_postgresql_database_url.

Technologies Used
Backend Framework: Django Rest Framework
Database: PostgreSQL
GraphQL API: AniList API
Authentication: JWT (JSON Web Token)
