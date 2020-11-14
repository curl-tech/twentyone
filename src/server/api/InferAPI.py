from flask import Blueprint

infer_api = Blueprint('infer_api', __name__)

@infer_api.route("/infer")
def infer():
    return "Infer Response"