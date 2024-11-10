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
    glossary = [
        {'term': 'Lorem', 'defenition': 'Далеко-далеко за словесными горами, в стране гласных и согласных живут рыбные тексты.'},
        {'term': 'Labore', 'defenition': 'Проектах это парадигматическая, выйти lorem его встретил то!'},
        {'term': 'Iste', 'defenition': ' Текста вдали языкового ведущими переулка, океана страна живет правилами жаренные пустился букв осталось рекламных грустный послушавшись ее на берегу которое прямо что!'},
        {'term': 'Doloribus', 'defenition': 'Прямо бросил на берегу, напоивший подпоясал, правилами букв обеспечивает заглавных грустный строчка журчит, страну запятых текста снова?'},
        {'term': 'Aut', 'defenition': 'О безопасную пунктуация, жаренные сих предупредила рыбного!'},
    ]


    # Сортируем глоссарий по алфавиту
    glossary = sorted(glossary, key=lambda d: d["term"])
    
    return render_template("glossary.html", name="Глоссарий", glossary=glossary)
