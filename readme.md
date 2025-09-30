# 📌 Simple Blog API (FastAPI)

This is a simple REST API built with **FastAPI** that allows users to:
- Create a post
- Like a post
- Comment on a post
- Fetch all posts

The project uses an **in-memory database (Python dictionary)** for storing posts.

---

## 🚀 Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
(Optional) Create and activate a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Linux/Mac
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the API:

bash
Copy code
uvicorn main:app --reload
Open your browser and visit:

arduino
Copy code
http://127.0.0.1:8000/docs
(Interactive Swagger UI provided by FastAPI)

📖 API Endpoints
1️⃣ Create a Post
POST /posts/
Request Body:

json
Copy code
{
  "id": 1,
  "title": "First Post",
  "content": "Hello, this is my first post!"
}
2️⃣ Like a Post
POST /posts/{post_id}/like

3️⃣ Comment on a Post
POST /posts/{post_id}/comment?comment=Nice%20post!

4️⃣ Get All Posts
GET /posts/

Response:

json
Copy code
[
  {
    "id": 1,
    "title": "First Post",
    "content": "Hello, this is my first post!",
    "likes": 1,
    "comments": ["Nice post!"]
  }
]
📦 Tech Stack
FastAPI

Pydantic

Uvicorn

✨ Future Improvements
Add persistent database (SQLite, PostgreSQL, MongoDB)

Add user authentication

Add update & delete functionality

yaml
Copy code
