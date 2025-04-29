from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

#import local modules
from .crud import get_all_notes, create_note

#Start the Application
app = FastAPI()

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    """
    Root endpoint that returns a welcome message.

    This endpoint is used to check if the API is running.
    """
    return templates.TemplateResponse("index.html", {"request": request})
    #return {"message": "Welcome to the Notes API!"}

@app.get("/notes", response_class=HTMLResponse)
def read_notes(request: Request):
    """
    Endpoint to retrieve all notes and render them in an HTML template.

    :param request: The request object.
    :return: Rendered HTML page with notes.
    """
    notes = get_all_notes()
    return templates.TemplateResponse("notes.html", {"request": request, "notes": notes})


#if we ever run directily from this file, we can run the app with uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)