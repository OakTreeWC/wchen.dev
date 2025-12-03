from pathlib import Path
from flask import Flask, render_template, jsonify


BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"


app = Flask(__name__, template_folder=str(TEMPLATES_DIR), static_folder=str(STATIC_DIR))

@app.route("/")
def index():
        return render_template("index.html")

@app.route("/about")
def about():
        return render_template("about.html")

@app.route("/projects")
def projects():
        return render_template("projects.html")

@app.route("/api/status")
def api_status():
        return jsonify(status="ok", message="Flask app running")

if __name__ == "__main__":
        app.run(debug=False, host="0.0.0.0", port=80)