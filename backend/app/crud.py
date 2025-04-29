from .models import *

# In-memory storage for notes (for demonstration purposes)
notes = [
    {'id': 1, 'title': "Sample Note 1", 'content': "This is a sample note."},
    {'id': 2, 'title': "Sample Note 2", 'content': "This is a sample note."},
    {'id': 3, 'title': "Sample Note 3", 'content': "This is a sample note."},
    {'id': 4, 'title': "Sample Note 4", 'content': "This is a sample note."},
]

def create_note(note: Note):
    """
    Create a new note.
    :param note: The note to create.
    """
    notes.append(note)
    return note

def get_all_notes():
    """
    Get all notes.
    :return: A list of all notes.
    """
    return notes