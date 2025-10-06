import json
import os

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
    """Handle adding a new blog post via form with validation."""
    if request.method == "POST":
        posts = load_posts()

        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        author = request.form.get("author", "Anonymous").strip() or "Anonymous"

        if not title or not content:
            error_msg = "Title and content cannot be empty."
            return render_template("add.html", error=error_msg)

        new_id = max((post["id"] for post in posts), default=0) + 1

        new_post = {
            "id": new_id,
            "author": author,
            "title": title,
            "content": content,
            "likes": 0
        }

        posts.append(new_post)
        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("add.html")


@app.route("/delete/<int:post_id>", methods=["GET"])
def delete(post_id):
    """Delete a post by ID (GET method required by assignment)."""
    posts = load_posts()
    updated_posts = [post for post in posts if post["id"] != post_id]

    if len(updated_posts) == len(posts):
        return "Post not found", 404

    save_posts(updated_posts)
    return redirect(url_for("index"))


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Update an existing post safely."""
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        author = request.form.get("author", "").strip()

        if not title or not content:
            error_msg = "Title and content cannot be empty."
            return render_template("update.html", post=post, error=error_msg)

        updated_post = {
            "id": post["id"],
            "author": author or post["author"],
            "title": title or post["title"],
            "content": content or post["content"],
            "likes": post.get("likes", 0)
        }

        posts = [updated_post if p["id"] == post_id else p for p in posts]
        save_posts(posts)
        return redirect(url_for("index"))

    return render_template("update.html", post=post)


@app.route("/like/<int:post_id>", methods=["POST"])
def like(post_id):
    """Increment likes for a post, with validation."""
    posts = load_posts()
    post = next((p for p in posts if p["id"] == post_id), None)

    if post is None:
        return "Post not found", 404

    post["likes"] = post.get("likes", 0) + 1
    save_posts(posts)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
