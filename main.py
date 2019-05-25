from flask import Flask, request as flaskreq
from msgtype import msgtype
from starting import starting
from logcsv import logcsv


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    data = flaskreq.json
    # print(data)
    resp = msgtype(data)
    logcsv(data, resp)
    return '', 200


# If run on local machine:
starting()
if __name__ == '__main__':
    app.run(host='localhost', port=10568, debug=False)
