from flask import Flask, render_template, request

from utils import models, procesar_pregunta
from dotenv import load_dotenv
import os

load_dotenv()

port = os.getenv('port')

app = Flask(__name__, template_folder="templates")


# @app.before_first_request
def load_models():
    models()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/respond', methods=['POST'])
def respuesta_chatbot():
    pregunta = next(request.form.values())
    # titulo = request.form['titulo']

    respuesta = procesar_pregunta(pregunta)

    return render_template('index.html', Category=respuesta)


if __name__ == "__main__":
    load_models()
    app.run(host='0.0.0.0', port=port)
