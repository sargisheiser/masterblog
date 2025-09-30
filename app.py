import os
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_FILE = os.path.join(BASE_DIR, "posts.json")

def load_posts():
   """Load blog posts from the JSON file, or return empty list if missing."""
   try:
       with open(POSTS_FILE, "r", encoding="utf-8") as f:
           return json.load(f)
   except FileNotFoundError:
       return []

def save_posts(posts):
   """Save blog posts to the JSON file."""
   with open(POSTS_FILE, "w", encoding="utf-8") as f:
       json.dump(posts, f, indent=4)

@app.route("/")
def index():
   """Render homepage with all blog posts."""
   blog_posts = load_posts()
   return render_template("index.html", posts=blog_posts)
@app.route("/add", methods=["GET", "POST"])
def add():
   """Handle adding a new blog post via form."""
   if request.method == "POST":
       posts = load_posts()


       new_id = max((post["id"] for post in posts), default=0) + 1

       new_post = {
           "id": new_id,
           "author": request.form.get("author", "Anonymous"),
           "title": request.form.get("title", "Untitled"),
           "content": request.form.get("content", "")
       }

       posts.append(new_post)
       save_posts(posts)

       return redirect(url_for("index"))

   return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
   posts = load_posts()
   updated_posts = [post for post in posts if post["id"] != post_id]
   save_posts(updated_posts)
   return redirect(url_for("index"))

@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        post["author"] = request.form.get("author", post["author"])
        post["title"] = request.form.get("title", post["title"])
        post["content"] = request.form.get("content", post["content"])

        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("update.html", post=post)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5002, debug=True)
