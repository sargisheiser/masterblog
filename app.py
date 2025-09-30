import json
from flask import Flask, render_template

app = Flask(__name__)


def load_posts():
    """Load blog posts from the JSON file."""
    with open("posts.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    """Render homepage with all blog posts."""
    blog_posts = load_posts()
    return render_template("index.html", posts=blog_posts)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


