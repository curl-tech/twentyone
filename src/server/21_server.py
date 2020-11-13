# We will implement it in Flask to make if simple and fast

import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/data_upload', methods=['POST'])
def data_upload():
    return 'Uploaded!'

# Low priority now
@app.route('/data_req', methods=['GET', 'POST'])
def data_req():
    return 'view'

@app.route('/new_task', methods=['POST'])
def new_task():
    return 'Task Completed!'

@app.route('/get_model', methods=['GET'])
def get_model():
    return 'model'

# don't implement now
@app.route('/model_upload', methods=['POST'])
def model_upload():
    return 'uploaded'

@app.route('/infer', methods=['POST'])
def infer():
    return 'prediction'