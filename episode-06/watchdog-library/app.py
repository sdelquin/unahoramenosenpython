import uuid
import json
from html import escape
from pathlib import Path

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
        'b { color: white; }',
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
        as_messages_list(),
        '</html>',
    ])


@app.route("/post/", methods=['POST'])
def post_message():
    name = request.form['name']
    message = request.form['message']
    if message:
        filename = f'{uuid.uuid4().hex}.json'
        with open(filename, 'w', encoding='utf-8') as fout:
            json.dump({
                "name": name or "Anonymous",
                "message": message,
                }, fout
            )
    return redirect("/")


def get_all_messages():
    all_files = sorted(
        Path('.').iterdir(),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )
    for filename in all_files:
        if filename.name.endswith('.json'):
            with open(filename, encoding="utf-8") as fin:
                yield json.load(fin)


def as_messages_list():
    buff = [
        format('<p><b>{name}</b> says: <tt><b>{message}</b></tt></p>'.format(
            name=escape(msg['name']),
            message=escape(msg['message'])
        ))
        for msg in get_all_messages()
    ]
    return "\n".join(buff)


