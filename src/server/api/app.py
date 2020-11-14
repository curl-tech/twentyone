from flask import Flask, jsonify, request
# from flask.ext.store import Store
import json

from DataUploadAPI import data_upload_api
from DataReqAPI import data_req_api
from NewTaskAPI import new_task_api
from GetModelAPI import get_model_api
from InferAPI import infer_api
from ModelUploadAPI import model_upload_api

import os

app = Flask(__name__)
# app.config['STORE_DOMAIN'] = 'http://127.0.0.1:5000'
# app.config['STORE_PATH'] = '/some/path/to/somewhere'
# store = Store(app)

app.register_blueprint(data_upload_api)
app.register_blueprint(data_req_api)
app.register_blueprint(new_task_api)
app.register_blueprint(get_model_api)
app.register_blueprint(infer_api)
app.register_blueprint(model_upload_api)

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def home():
    return "21 APIs"

@app.route("/livecheck", methods=['GET'])
def livecheck():
    return "Server is online"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')