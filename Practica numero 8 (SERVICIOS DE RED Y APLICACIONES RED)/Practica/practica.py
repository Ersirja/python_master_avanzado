from flask as Flask

app = Flask(__name__)

@app.route('/')

def hola_mundo():
    return "hola mundo"



