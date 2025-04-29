notes = []

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