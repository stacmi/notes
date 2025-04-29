# Notes Web Application

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple full-stack web application for creating, viewing, updating, and deleting notes.  
Built with **FastAPI** for the backend and **vanilla JavaScript/HTML/CSS** for the frontend.

## 🚀 Features
- RESTful API supporting Create, Read, Update, and Delete (CRUD) operations on notes
- Lightweight frontend interface for interacting with the backend
- Modular backend structure following clean code principles
- Fast development with asynchronous server support

## 🛠️ Technologies Used
- Python
- FastAPI
- Uvicorn
- JavaScript
- HTML/CSS

## 📦 Project Structure
```bash
notes/
├── backend/
│   ├── app/
│   │   ├── __init__.py     
│   │   ├── main.py         # FastAPI app and route setup
│   │   ├── models.py       # Data models (e.g., Note schema)
│   │   ├── crud.py         # Functions for creating, reading, updating, deleting notes
│   │   ├── database.py     # In-memory "database" or database interactions
│   └── requirements.txt
├── frontend/               # Frontend assets (CSS, JS)
│   ├── index.html
│   ├── script.js
│   └── style.css
```

# ⚙️ Getting Started

## Prerequisites
- Python 3.10+
- Git

## Installation
### 1. Clone the Repository
Fork the repository (optional)

- If you do this step replace "stacmi" with your own username

```bash
git clone https://github.com/stacmi/notes.git
cd notes
```

### 2. (Optional but recommended) Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows (not tested by me)
```
While on Linux typing `deactive` while in the venv will take you out of it

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the server
```bash
uvicorn backend.app.main:app --reload
```

### 5. Open your browser and visit:
```bash
http://127.0.0.1:8000   #Frontend will make calls to the backend API.
```

# ✏️ Future Improvements
-Add user authentication

-Persist notes using a real database (e.g., SQLite, PostgreSQL)

-Deploy the app to a cloud provider (e.g., Render, Vercel, or AWS)

-Add API testing and frontend form validation

-Improve UI with a frontend framework (optional)

---
---

# 📄 License

This project is open-source and available under the [MIT License](LICENCE).