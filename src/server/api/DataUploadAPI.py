from flask import Blueprint

data_upload_api = Blueprint('data_upload_api', __name__)

@data_upload_api.route("/data_upload")
def data_upload():
    return "Data Upload Response"