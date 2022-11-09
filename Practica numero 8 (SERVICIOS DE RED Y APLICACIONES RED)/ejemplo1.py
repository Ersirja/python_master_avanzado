from flask import Flask
app = Flask (__name__)
@app.route('/')

def principal():
    return "<h3>Hola mundo con Flask</h3>"

if __name__=='__main__':
    app.run()