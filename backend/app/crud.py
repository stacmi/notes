from models import Note

# In-memory storage for notes (for demonstration purposes)
notes = [{id: 1, title: "Sample Note", content: "This is a sample note."}]

def create_note(note: Note):
    """
    Create a new note.
    :param note: The note to create.
    """
    notes.append(note)
    return note

def get_notes():
    """
    Get all notes.
    :return: A list of all notes.
    """
    return notes