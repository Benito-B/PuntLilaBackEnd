from flask import Flask, jsonify, request, json
from gevent.pywsgi import WSGIServer
from puntLilaAPI.ServerUtils import *
from puntLilaAPI.config import SERVER_IP, SERVER_PORT, firebase_config
from flask_cors import CORS, cross_origin
import pyrebase

app = Flask(__name__)
cors = CORS(app, headers='Content-Type')
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()


@app.route('/authorize', methods=['POST'])
@cross_origin()
def authorize() -> json:
    """
    This endpoint '/authorize' only accepts POST method and expects a JSON payload with 'token', which will be the ID
    token generated by googleOauth. It checks the token for validity and then checks if the user is an admin on the
    system. Will return a JSON with the admin ID or an 'error' message.
    """
    # Get the data from the request
    data = request.json
    # This will return the id from the token or None if it is invalid
    admin_id = is_valid_user(data["token"])
    if admin_id is not None:
        # If it is not none and the user is also an admin return a code 200 and the id
        if user_is_admin(admin_id):
            return jsonify(id=admin_id), 200
        # If the user is not an admin return error 403
        return jsonify(error="L'usuari no és administrador"), 403
    # If the user token isn't valid, return error 401
    return jsonify(error="Usuari no vàlid!!"), 401


@app.route('/admins', defaults={'admin': None}, methods=['POST', 'GET', 'PUT', 'DELETE'])
@app.route('/admins/<admin>', methods=['POST', 'GET', 'PUT', 'DELETE'])
@cross_origin()
def manage_admins(admin: str) -> json:
    if request.method == "GET":
        # If using GET verb and no admin is indicated, get full list of admins. Otherwise, get info of the specified one
        if admin is not None:
            returning = db.child('admins').child(admin).get().val()
            if returning is not None:
                return jsonify(returning), 200
            return jsonify(error="Admin not found"), 404
        else:
            returning = db.child('admins').get().val()
            if returning is not None:
                return jsonify(returning), 200
            return jsonify(error="Database is empty"), 404

    elif request.method == "POST" or request.method == "PUT":
        # If method is post we expect to receive the email of the new admin and the email of who made him admin
        data = request.json
        try:
            email = data['email']
            admin_by = data['loggedUserEmail']
        except TypeError as err:
            print("[ERROR] An exception ocurred, type: {}, cause: {}".format(err.__class__.__name__, err.__cause__))
            return jsonify(error='Missing admin email (email) or loggedUserEmail'), 400
        store_data = {"added_by": admin_by}
        # Store the admin using his email as key
        db.child('admins').child(email).set(store_data)
        return jsonify(db.child('admins').child(email).get().val()), 201

    elif request.method == "DELETE":
        # If verb is DELETE, delete specified admin and return the whole list again
        if admin is not None:
            db.child('admins').child(admin).remove()
            return jsonify(db.child('admin').get().val()), 200
        else:
            return jsonify(error="No admin indicated in the route"), 400
    """
    This endpoint '/admins/<admin>' works with POST, GET, PUT AND DELETE. With the POST and PUT methods
     it expects a JSON payload with 'email' and 'loggedUserEmail'.
     Always returns a JSON with the changes made/new data
    """


@app.route('/phones', defaults={'phone': None}, methods=['POST', 'GET', 'PUT', 'DELETE'])
@app.route('/phones/<phone>', methods=['POST', 'GET', 'PUT', 'DELETE'])
@cross_origin()
def manage_phonenumbers(phone: str) -> json:
    """
    This endpoint '/phones/<phone>' works with POST, GET, PUT AND DELETE. With the POST and PUT methods
     it expects a JSON payload with 'phone' and 'loggedUserEmail'.
     Always returns a JSON with the changes made/new data
    """
    if request.method == "POST" or request.method == "PUT":
        # If method is post or put we expect to receive the new number to be added, the description
        # and the email of the admin adding it
        data = request.json
        phone_number = phone
        try:
            phone_description = data['description']
            added_by = data['loggedUserEmail']
        except TypeError as err:
            print("[ERROR] An exception ocurred, type: {}, cause: {}".format(err.__class__.__name__, err.__cause__))
            return jsonify(error='Missing description or loggedUserEmail'), 400
        store_data = {"description": phone_description,
                      "added_by": added_by}
        db.child('phones').child(phone_number).set(store_data)

        return jsonify(db.child('phones').child(phone).get().val()), 201

    elif request.method == "GET":
        # If using GET verb and no number is indicated, get full list. Otherwise, get info of the specified one
        if phone is not None:
            returning = db.child('phones').child(phone).get().val()
            if returning is not None:
                return jsonify(returning), 200
            return jsonify(error="Phone not found"), 404
        else:
            returning = db.child('phones').get().val()
            if returning is not None:
                return jsonify(returning), 200
            return jsonify(error="Database is empty"), 404

    elif request.method == "DELETE":
        # If verb is DELETE, delete the specified number and return the list again
        if phone is not None:
            db.child('phones').child(phone).remove()
            return jsonify(db.child('phones').get().val()), 200
        else:
            return jsonify(error="No phone indicated in the route"), 400


@app.route('/notifications', defaults={'phone': None}, methods=['POST'])
def manage_notifications() -> json:
    """
    This endpoint '/notifications' expects to receive a JSON with a 'message' and a 'loggedUserEmail' and will push
    the message to the database using a timestamp as a key storing the email of the creator in a child named 'sent_by'
    Always returns a JSON with the changes made/new data
    """
    data = request.json
    message = data['message']
    sent_by = data['loggedUserEmail']
    if message is not None:
        # If the message is not empty push it to the database (Push uses an autogenerated timestamp based key)
        return jsonify(message="Notification sent by: {} - {}".format(sent_by, message))
    return jsonify(error="Empty message")


if __name__ == '__main__':
    http_server = WSGIServer((SERVER_IP, SERVER_PORT), app)
    print("Starting server on {}:{}".format(SERVER_IP, SERVER_PORT))
    http_server.serve_forever()
