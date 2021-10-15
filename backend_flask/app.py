from flask import Flask , jsonify
from ml import *

app =  Flask(__name__)

@app.route('/')
def index():
    result = result_score()
    return jsonify(result)


if __name__ == "__main__" :
    app.secret_key = "secret1234"
    app.run(debug=True)
