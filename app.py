import requests
from flask import Flask, jsonify

app = Flask(__name__)

# ✅ ROOT ROUTE (fixes Render 404)
@app.route('/')
def home():
    return jsonify({
        "message": "Flask API is live on Render 🚀",
        "endpoints": [
            "/posts",
            "/comments",
            "/albums",
            "/posts/<id>/comments"
        ]
    })

# ✅ GET POSTS
@app.route('/posts')
def get_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    return jsonify({
        "data": response.json(),
        "status": "success",
        "status_code": response.status_code
    })

# ✅ GET COMMENTS
@app.route('/comments')
def get_comments():
    response = requests.get("https://jsonplaceholder.typicode.com/comments")
    return jsonify({
        "data": response.json(),
        "status": "success",
        "status_code": response.status_code
    })

# ✅ GET ALBUMS
@app.route('/albums')
def get_albums():
    response = requests.get("https://jsonplaceholder.typicode.com/albums")
    return jsonify({
        "data": response.json(),
        "status": "success",
        "status_code": response.status_code
    })

# ✅ GET COMMENTS BY POST ID (dynamic route)
@app.route('/posts/<int:post_id>/comments')
def get_post_comments(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    return jsonify({
        "data": response.json(),
        "status": "success",
        "status_code": response.status_code
    })

# ✅ RUN (for local only)
if __name__ == '__main__':
    app.run(debug=True)
