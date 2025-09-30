import os
import json
from flask import Flask, render_template

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

@app.route("/")
def index():
   """Render homepage with all blog posts."""
   blog_posts = load_posts()
   return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5002, debug=True)
