from flask import Flask, jsonify, request ,send_file, make_response
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from werkzeug.security import generate_password_hash, check_password_hash
from ml import result_score
from digits import do_plot
from testing_mnist import test


app = Flask(__name__)
app.secret_key = "secret123"
app.config["MONGO_URI"] = "mongodb://localhost:27017/Users"
mongo = PyMongo(app)


@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if (_name and _email and _password and request.method == "POST"):
        _hashed_password = generate_password_hash(_password)
        id = mongo.db.user.insert({
            'name': _name,
            'email': _email,
            'pwd': _hashed_password
        })

        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()


@app.route('/users')
def users():
    users = mongo.db.user.find()
    resp = dumps(users)
    return resp


@app.route('/users/<id>')
def user(id):
    user = mongo.db.user.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp


@app.route('/delete/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.user.delete_one({'_id': ObjectId(id)})
    response = jsonify("User Deleted successfully")
    response.status = 200
    return response


@app.route('/register', methods=["POST", "GET"])
def register():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    user = mongo.db.user.find_one({'email': _email})
    if(user):
        resp = jsonify("User already exists")
        return resp

    else:

        if (_name and _email and _password and request.method == "POST"):
            _hashed_password = generate_password_hash(_password)
            id = mongo.db.user.insert({
                'name': _name,
                'email': _email,
                'pwd': _hashed_password
            })
            resp = jsonify("User Registered successfully")
            resp.status_code = 200
            return resp
        else:
            return not_found()


@app.route('/update/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _pwd = _json['pwd']
    if(_name and _email and _pwd and id and request.method == "PUT"):
        _hashed_password = generate_password_hash(_pwd)
        mongo.db.user.update_one({
            '_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
            {'$set': {
                'name': _name,
                'email': _email,
                'pwd': _hashed_password,
            }}
        )
        resp = jsonify("User Updated successfully")
        resp.status = 200
        return resp
    else:
        return not_found()


@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }

    resp = jsonify(message)
    resp.status_code = 404
    return resp


@app.route('/show_result')
def show_result():
    result = test()[1]
    return jsonify(result)

@app.route('/plot')
def show_plot():
    bytes_obj = test()[0]
    result =  test()[1]
    return send_file(bytes_obj,
                     attachment_filename='plot.png',
                     mimetype='image/png')
    

if __name__ == "__main__":
    app.run(debug=True)
