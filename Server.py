from flask import Flask, jsonify, request
from gevent.pywsgi import WSGIServer
from puntLilaAPI.ServerUtils import *
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, headers='Content-Type')


@app.route('/authorize', methods=['POST'])
@cross_origin()
def authorize():
    data = request.json
    id = is_valid_user(data["token"])
    if id is not None:
        if user_is_admin(id):
            return jsonify(id=id), 200
        return jsonify(error="L'usuari no és administrador"), 403
    return jsonify(error="Usuari no vàlid!!"), 401


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
