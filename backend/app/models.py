from pydantic import BaseModel

class Note(BaseModel):
    """
    A note model representing a note in the application.
    """
    id: int
    title: str
    content: str
    created_at: str
    updated_at: str


# Just a thought for later if/when I add authentication
#class User(BaseModel):
#    id: int
#    username: str
#    email: str
#    full_name: str