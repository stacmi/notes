from fastapi import FastAPI
from models import Note

app = FashtAPI()

@app.get("/")
def add_note():
    """
    Root endpoint that returns a welcome message.

    This endpoint is used to check if the API is running.
    """
    return {"message": "Welcome to the Notes API!"}

@app.get("/notes/")
def get_notes():
    """
    Endpoint to retrieve all notes.

    Returns a list of all notes in the system.
    """
    return get_notes()