import os
from flask import Flask, render_template, abort, request

# Use absolute paths so it works regardless of working directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'templates'),
    static_folder=os.path.join(BASE_DIR, 'public'),
    static_url_path=''
)

PAINTINGS = [
    {
        "id": 1,
        "title": "Portretas profiliu",
        "technique": "Aliejus ant drobės",
        "price": "Kaina sutartinė",
        "image": "/assets/paveikslas1.jpg",
        "description": "Šis klasikinis profilio portretas spinduliuoja ramybe ir vidiniu susikaupimu. Subtilūs aliejinių dažų potėpiai kuria gylio ir paslapties įspūdį. Puikiai tiks tiek moderniame, tiek klasikiniame interjere kaip dėmesį traukiantis akcentas."
    },
    {
        "id": 2,
        "title": "Skriejanti figūra",
        "technique": "Eskizas / Grafika",
        "price": "Kaina sutartinė",
        "image": "/assets/paveikslas2.jpg",
        "description": "Ekspresyvus eskizas, kuriame fiksuojama judesio dinamika ir laisvė. Švelnios, bet tvirtos linijos atspindi žmogaus kūno plastiką. Tai kūrinys, kuris įkvepia energijos ir tinka minimalistinėms, šviesioms erdvėms."
    },
    {
        "id": 3,
        "title": "Figūra (Aktas)",
        "technique": "Pieštukas / Anglis",
        "price": "Kaina sutartinė",
        "image": "/assets/paveikslas3.jpg",
        "description": "Meistriškai atliktas aktas, kuriame atsiskleidžia klasikinė žmogaus anatomijos studija. Anglies ir pieštuko kontrastai sukuria galingą šviesos ir šešėlio žaismą. Idealiai tinka darbo kambariui ar privačiai galerijos erdvei."
    },
    {
        "id": 4,
        "title": "Vakaro peizažas",
        "technique": "Aliejus ant drobės",
        "price": "Kaina sutartinė",
        "image": "/assets/paveikslas4.jpg",
        "description": "Atmosferiškas vakaro peizažas, panardinantis į gamtos ramybę ir melancholiją. Tamsūs, sodrūs tonai ir paslaptingai krentanti šviesa kviečia apmąstymams. Tai kūrinys, kuris erdvei suteiks jaukumo ir gylio."
    },
    {
        "id": 5,
        "title": "Upės slėnis",
        "technique": "Aliejus ant drobės",
        "price": "Kaina sutartinė",
        "image": "/assets/paveikslas5.jpg",
        "description": "Atviras ir šviesus gamtos motyvas, fiksuojantis besikeičiančios upės vagos grožį. Švelnūs spalvų perėjimai sukuria gaivumo ir ramybės jausmą. Paveikslas atgaivins svetainės ar miegamojo interjerą, įnešdamas dalelę gamtos."
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', paintings=PAINTINGS)

@app.route('/painting/<int:painting_id>')
def painting(painting_id):
    p = next((p for p in PAINTINGS if p['id'] == painting_id), None)
    if not p:
        abort(404)
    return render_template('painting.html', painting=p)

@app.route('/contact')
def contact():
    subject = request.args.get('subject', '')
    return render_template('contact.html', prefilled_subject=subject)
