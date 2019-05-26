from flask import Flask, request as flask_req
from botSession import dra, dp
from telegram import Update

from starting import starting


app = Flask(__name__)


starting()


@app.route('/', methods=['POST'])
def main():
    update = Update.de_json(flask_req.json, dra)
    dp.process_update(update)
    return '', 200


@app.route('/', methods=['GET'])
def status():
    return '@Dragalia_bot is online.', 200


# If run on local machine:
if __name__ == '__main__':
    app.run(host='localhost', port=10568, debug=False)
