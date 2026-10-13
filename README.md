# AI Health Assistant

A FastAPI-based health assistant that provides a chat API endpoint for processing user messages.

## Prerequisites

- Python 3.9+ installed
- Git (optional)
- `pip` available

## Setup

1. Open a terminal and navigate to the project folder:

```powershell
cd c:\Users\urban\Downloads\ai-health-assistant
```

2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

## Initialize database

Run the database initializer to create required tables:

```powershell
python create_db.py
```

## Run the application

Start the FastAPI server with Uvicorn:

```powershell
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will be available at:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`

## API Usage

Use the chat endpoint to send a message:

```http
POST /api/chat
Content-Type: application/json

{
  "message": "Hello, I need health advice"
}
```

Example using `curl`:

```powershell
curl -X POST "http://127.0.0.1:8000/api/chat" -H "Content-Type: application/json" -d '{"message":"Hello"}'
```

## Tests

If you want to run tests, use:

```powershell
pytest tests
```
