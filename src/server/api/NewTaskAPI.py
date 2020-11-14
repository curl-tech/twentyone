from flask import Blueprint

new_task_api = Blueprint('new_task_api', __name__)

@new_task_api.route("/new_task")
def new_task():
    return "New Task API Response"