Podcast Episode Alternative Text Generator API

Overview

This project is a FastAPI-based API service for managing podcast episodes and generating alternative titles or descriptions using Google Gemini generative AI. It allows you to create podcast episodes, list all episodes, and generate alternative text for episode titles or descriptions.

⸻

Features
	•	List all podcast episodes
	•	Add new podcast episodes with validation to prevent duplicates
	•	Generate AI-powered alternative text for episode titles or descriptions
	•	PostgreSQL as the database backend with SQLAlchemy ORM
	•	Clear error handling with appropriate HTTP status codes

⸻

Tech Stack and Decisions
	•	FastAPI: Modern, fast web framework ideal for building APIs with automatic docs.
	•	SQLAlchemy: Powerful ORM for interacting with PostgreSQL, enabling easier data management.
	•	PostgreSQL: Reliable and scalable relational database.
	•	Google Gemini (generativeai): State-of-the-art generative AI for alternative text generation.
	•	Pydantic: Data validation and serialization, using Config with from_attributes = True to support model creation from ORM objects.
	•	Uvicorn: ASGI server to run the FastAPI app.

⸻

Setup and Installation

Prerequisites
	•	Python 3.10+
	•	PostgreSQL database running
	•	Google Gemini API key (set in .env file)

Clone the repository

git clone https://github.com/yourusername/podcast-ai-api.git
cd podcast-ai-api


Create and activate virtual environment

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows


Install dependencies

pip install -r requirements.txt


Set environment variables
Create a .env file in the project root with the following:

DATABASE_URL=postgresql+psycopg2://root:password@localhost:5432/project_db
GEMINI_API_KEY=your_google_gemini_api_key_here


Replace with your actual PostgreSQL credentials and Gemini API key.

Initialize the database

Make sure your PostgreSQL server is running and the database exists (project_db in example). You may need to create the database manually.

Run your migration or create tables via SQLAlchemy ORM models.

⸻

Running the Application
Start the FastAPI server using Uvicorn:

uvicorn main:app --reload

	•	The API will be available at http://127.0.0.1:8000
	•	Interactive API docs at http://127.0.0.1:8000/docs


API Endpoints

Get all episodes
	•	Endpoint: GET /episodes
	•	Response: List of episodes

Example request:
curl http://127.0.0.1:8000/episodes
Example response:
[
  {
    "title": "Building a Startup",
    "description": "Tips and lessons learned from successful founders on building your own tech company from scratch.",
    "host": "Alex Smith"
  },
  ...
]


Create a new episode
	•	Endpoint: POST /episodes
	•	Body:
{
  "title": "Building a Startup",
  "description": "Tips and lessons learned from successful founders on building your own tech company from scratch.",
  "host": "Alex Smith"
}
	•	Responses:
	•	200 OK with created episode
	•	400 Bad Request if episode title already exists



Generate alternative text for an episode
	•	Endpoint: POST /episodes/{episode_id}/generate_alternative
	•	Path parameter:
	•	episode_id (int) - ID of the episode to generate alternative for
	•	Body:
{
  "target": "description",
  "prompt": "Summarize this description for busy professionals."
}
	•	Responses:
	•	200 OK with alternative text
	•	404 Not Found if episode not found
	•	400 Bad Request if invalid target

Example response:
{
  "original_episode": {
    "title": "Building a Startup",
    "description": "Tips and lessons learned from successful founders on building your own tech company from scratch.",
    "host": "Alex Smith"
  },
  "target": "description",
  "prompt": "Summarize this description for busy professionals.",
  "generated_alternative": "Startup wisdom in 15 minutes: what works, what doesn't."
}


Error Handling
	•	If an episode with a given ID does not exist, the API returns:
{
  "detail": "Episode not found"
}

with HTTP status code 404.
	•	Duplicate episode titles when creating new episodes return:
{
  "detail": "Episode with title '...' already exist."
}
with HTTP status code 400.


Notes
	•	The project uses Pydantic models with from_attributes = True for smooth ORM integration.
	•	The Google Gemini API key must be valid for the AI text generation feature to work.
	•	Database connection string must match your PostgreSQL setup.
	•	The app can be extended with authentication, pagination, or more episode fields as needed.