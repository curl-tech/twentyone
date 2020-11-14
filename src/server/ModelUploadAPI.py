from flask import Blueprint

model_upload_api = Blueprint('model_upload_api', __name__)

# Later
@model_upload_api.route("/model_upload")
def model_upload():
    return "Model Upload Response"