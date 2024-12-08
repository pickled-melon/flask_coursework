from flask import Flask, render_template

app = Flask(__name__)

nav = [
    {"title": "Главная", "URL": "/"},
    {"title": "История", "URL": "/history"},
    {"title": "Функции", "URL": "/features"},
    {"title": "Будущее", "URL": "/future"},
    {"title": "Глоссарий", "URL": "/glossary"},
    {"title": "Об авторе", "URL": "/about"},
]

@app.context_processor
def global_context():
    return {
        "nav": nav,
    }

@app.route("/")
def index_page():
    cards = [
        {"title": "История и создание", "URL": "/history", "img_link": "/static/images/world_bank_logo.jpg", "img_alt": "Логотип Всемирного банка", "desc": "Всемирный банк был основан в 1944 году на Бреттон-Вудской конференции с целью содействия экономическому восстановлению и развитию после Второй мировой войны."},
        {"title": "Функции Всемирного банка", "URL": "/features" , "img_link": "/static/images/world_bank_features.jpg", "img_alt": "Функции Всемирного банка", "desc": "Всемирный банк предоставляет кредиты и гранты для финансирования проектов, направленных на развитие инфраструктуры, здравоохранения, образования, сельского хозяйства и других ключевых секторов экономики."},
        {"title": "Будущее Всемирного банка", "URL": "/future", "img_link": "/static/images/world_bank_future.jpg", "img_alt": "МВФ и земной шар", "desc": "Будущее Всемирного банка будет сосредоточено на устойчивом развитии и борьбе с изменением климата."},
    ]
    return render_template("index.html", name="Главная", cards=cards)

@app.route("/history")
def history_page():
    return render_template("history.html", name="История")

@app.route("/features")
def features_page():
    return render_template("features.html", name="Функции")

@app.route("/future")
def future_page():
    return render_template("future.html", name="Будущее")

@app.route("/about")
def about_page():
    return render_template("about.html", name="Об авторе")

@app.route("/glossary")
def glossary_page():
    glossary = [
        {'term': 'Всемирный банк', 'anchor':'world_bank', 'defenition': 'Международная финансовая организация со штаб-квартирой в Вашингтоне, предоставляющая кредиты, беспроцентные займы и гранты правительствам стран с низким и средним уровнем дохода с целью реализации капитальных проектов'},
        {'term': 'Бреттон-Вудская конференция', 'anchor': 'Bretton_Woods_Conference', 'defenition': 'Международная конференция, состоявшаяся в июле 1944 года в США, штат Нью-Гэмпшир, Бреттон-Вудс, отель «Маунт Вашингтон». Были подписаны соглашения о создании МВФ и МБРР (будущий Всемирный банк) и о принципах формирования валютных обменных курсов.'},
        {'term': 'Международная ассоциация развития', 'anchor': 'International_Development_Association', 'defenition': 'Кредитная организация, входящая в группу Всемирного банка. Создана в 1960 году. Цель организации — оказание помощи самым бедным странам за счёт добровольных пожертвований стран-членов. 1 Право на получение займов из МАР имеют страны с ВВП на душу населения не более \$1165. 1 Также МАР предоставляет помощь странам, которые не соответствуют критериям получения займов, но не обладают кредитоспособностью для получения кредитов от МБРР. '},
        {'term': 'Цели развития тысячелетия', 'anchor': 'Millennium_Development_Goals', 'defenition': 'Восемь международных целей развития, которые 193 государства-члена ООН и, по меньшей мере, 23 международные организации договорились достичь к 2015 году. Цель ЦРТ — ускорение развития путём улучшения социальных и экономических условий в беднейших странах мира. '},
        {'term': 'Цифровизация', 'anchor':'digitalization', 'defenition': 'Цифровая трансформация системы государственного управления и создание «электронного правительства». В более широком понимании — цифровая трансформация всего государственного сектора экономики. Главная цель цифровизации — это реформирование и улучшение государственного аппарата: оптимизация количества чиновников в госуправлении, борьба с бюрократизмом, казнокрадством, взяточничеством и коррупцией.'},
        {'term': 'Доклад о мировом развитии', 'anchor': 'World_Development_Report', 'defenition': 'Ежегодный доклад, публикуемый с 1978 года Всемирным банком. Каждый из докладов посвящён анализу конкретного аспекта экономического развития.'},
        {'term': 'Организация Объединённых Наций', 'anchor': 'United_Nations', 'defenition': 'Международная организация, созданная для поддержания и укрепления международного мира и безопасности, а также развития сотрудничества между государствами. Штаб-квартира ООН находится в Нью-Йорке; у ООН также есть дополнительные офисы в Вене, Женеве и Найроби. Международный суд ООН находится в Гааге. В структуру ООН входят шесть основных органов: Генеральная Ассамблея, Совет Безопасности, Экономический и Социальный Совет (ЭКОСОС), Совет по опеке, Международный суд ООН и Секретариат ООН.'},
        {'term': 'Международный валютный фонд', 'anchor':' International_Monetary_Fund', 'defenition': 'Специализированное учреждение Организации Объединённых Наций с главным офисом в городе Вашингтон, США. Это крупнейшая финансовая организация мира. Официальная дата создания МВФ — 27 декабря 1945 года. Фонд начал свою деятельность 1 марта 1947 года как часть Бреттон-Вудской системы. '},
        {'term': 'Изменение климата', 'anchor': 'Climate_change', 'defenition': 'Колебания климата Земли в целом или отдельных её регионов с течением времени, выражающиеся в статистически достоверных отклонениях параметров погоды от многолетних значений за период времени от десятилетий до миллионов лет.'},
        #{'term': '', 'anchor':'', 'defenition': ''},
        #{'term': 'Устойчивое развитие', 'defenition': 'Процесс экономических и социальных изменений, при котором природные ресурсы, направление инвестиций, ориентация научно-технического развития, развитие личности и институциональные изменения согласованы друг с другом и укрепляют нынешний и будущий потенциал для удовлетворения человеческих потребностей и устремлений.'},
        {'term': 'Инвестиции', 'anchor': 'Investment', 'defenition': 'Денежные средства, ценные бумаги, иное имущество, в том числе имущественные права, иные права, имеющие денежную оценку, вкладываемые в объекты предпринимательской и (или) иной деятельности в целях получения прибыли и (или) достижения иного полезного эффекта.'},
        #{'term': 'Финансирование на основе результатов', 'defenition': 'Подход, при котором финансирование проектов зависит от достижения заранее определенных результатов.'},
        #{'term': 'Анализ политики', 'defenition': 'Исследования и рекомендации, предоставляемые Всемирным банком для поддержки стран в разработке эффективной экономической политики.'},
        #{'term': 'Глобальное партнерство', 'defenition': 'Сотрудничество между Всемирным банком и другими международными организациями, правительствами и частным сектором для достижения общих целей развития.'},
    ]


    # Сортируем глоссарий по алфавиту
    glossary = sorted(glossary, key=lambda d: d["term"])

    return render_template("glossary.html", name="Глоссарий", glossary=glossary)
