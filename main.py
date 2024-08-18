from flask import Flask, render_template, url_for, request, g
app = Flask(__name__)

@app.before_request
def before_request():
    g.use_layout = request.headers.get("hx-request") != "true"

@app.route('/')
def index():
    return render_template("pages/home.html")

@app.route('/users')
def users():
    return render_template("pages/users.html")


@app.route('/posts')
def posts():
    return render_template("pages/posts.html")


if __name__ == "__main__":
    app.run(debug=True)
