from flask import Flask, render_template, url_for, request, g
app = Flask(__name__)

@app.before_request
def before_request():
    g.use_main_layout = request.headers.get("hx-request") != "true"

@app.route('/')
def index():
    return render_template("pages/dashboard/dashboard.html")

@app.route('/tasks')
def users():
    return render_template("pages/tasks/tasks.html")

if __name__ == "__main__":
    app.run(debug=True)
