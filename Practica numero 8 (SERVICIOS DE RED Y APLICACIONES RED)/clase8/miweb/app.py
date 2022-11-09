from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return "Hola mundoooo"


@app.route("/contacto")
def contacto():
    return "Este es mi contacto"

@app.route("/p/<string:content>")
def mostrar_info(content):
    return f"El titulo del post es {content}"
# if __name__ == '__main__':
#       app.run(host='0.0.0.0', port=80)