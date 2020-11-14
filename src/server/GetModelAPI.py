from flask import Blueprint

get_model_api = Blueprint('get_model_api', __name__)

# Later
@get_model_api.route("/get_model")
def get_model():
    return "Get Model Response"