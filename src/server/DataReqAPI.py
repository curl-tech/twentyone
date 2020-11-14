from flask import Blueprint

data_req_api = Blueprint('data_req_api', __name__)

# For later
@data_req_api.route("/data_req")
def data_req():
    
    return "Data Requirement Response"