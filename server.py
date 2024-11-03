from flask import Flask, render_template

app = Flask(__name__)

nav = [
    {"title": "Главная", "URL": "/"},
    {"title": "Об авторе", "URL": "/about"},
    {"title": "Глоссарий", "URL": "/glossary"},
]

@app.context_processor
def global_context():
    return {
        "nav": nav,
    }

@app.route("/")
def index_page():
    return render_template("index.html", name="Главная")

@app.route("/about")
def about_page():
    return render_template("about.html", name="Об авторе")

@app.route("/glossary")
def glossary_page():
    return render_template("glossary.html", name="Глоссарий")
