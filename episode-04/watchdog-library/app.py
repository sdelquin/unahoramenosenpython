import uuid
import json

from flask import Flask
from flask import redirect
from flask import request


app = Flask(__name__)


@app.route("/")
def index():
    return "\n".join([
        '<html>',
        '<head>',
        '<title>Mensajes con Watchdog</title>',
        '</head>',
        '<style>'
        'body {'
        '  background-color: #000000;',
        '  color: #33FF33;',
        '  font-weight:bolder;',
        '}',
        '</style>'
        '<body>',
        '<h1>Deja tu mensaje</h1>',
        '<form method="POST" action="/post/">',
        '<p>Tu nombre:</p>',
        '<input type="text" name="name">',
        '<p>Mensaje:</p>',
        '<textarea name="message" cols="72" rows="6"></textarea>',
        '<p></p>',
        '<input type="SUBMIT" name="ok" value="Enviar mensaje">',
        '<form>',
        '</html>',
    ])


@app.route("/post/", methods=['POST'])
def post_message():
    name = request.form['name']
    message = request.form['message']
    if message:
        filename = f'{uuid.uuid4().hex}.json'
        with open(filename, 'w') as fout:
            json.dump({
                "name": name or "Anonymous",
                "message": message,
                }, fout
            )
    return redirect("/")
