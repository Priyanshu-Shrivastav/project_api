from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# Data Models
class Post(BaseModel):
    id: int
    title: str
    content: str
    likes: int = 0
    comments: List[str] = []

# In-memory "database"
posts: Dict[int, Post] = {}

# 1️⃣ Create a Post
@app.post("/posts/")
def create_post(post: Post):
    if post.id in posts:
        raise HTTPException(status_code=400, detail="Post already exists!")
    posts[post.id] = post
    return {"message": "Post created successfully!", "post": post}

# 2️⃣ Like a Post
@app.post("/posts/{post_id}/like")
def like_post(post_id: int):
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Post not found!")
    posts[post_id].likes += 1
    return {"message": "Post liked!", "likes": posts[post_id].likes}

# 3️⃣ Comment on a Post
@app.post("/posts/{post_id}/comment")
def comment_post(post_id: int, comment: str):
    if post_id not in posts:
        raise HTTPException(status_code=404, detail="Post not found!")
    posts[post_id].comments.append(comment)
    return {"message": "Comment added!", "comments": posts[post_id].comments}

# 4️⃣ Get All Posts
@app.get("/posts/")
def get_posts():
    return list(posts.values())
