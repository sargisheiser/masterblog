📝 Flask Blog Application
A simple blog application built with Flask.
 This project demonstrates the basics of CRUD (Create, Read, Update, Delete) operations and includes a bonus Like button feature.

🚀 Features
📖 View all blog posts


➕ Add new blog posts


✏️ Edit existing blog posts


🗑 Delete blog posts


👍 Like blog posts (bonus feature)


Data persistence via JSON file



📂 Project Structure
Masterblog/
│
├── app.py              # Main Flask application
├── posts.json          # JSON file storing blog posts
│
├── templates/          # HTML templates
│   ├── index.html
│   ├── add.html
│   └── update.html
│
├── static/             # Static assets (CSS, images)
│   └── style.css
│
└── README.md           # Project documentation


⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/Masterblog.git
cd Masterblog

2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

3. Install dependencies
pip install flask

4. Run the app
python app.py

Open http://localhost:5000 in your browser.

🗃 Data Storage
All blog posts are stored in posts.json.
 Each post has the following structure:
{
  "id": 1,
  "author": "John Doe",
  "title": "First Post",
  "content": "This is my first post.",
  "likes": 0
}



