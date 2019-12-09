from flask import request, abort

from src.app import app

from datetime import datetime


def retrieve_requests(request_id=None):
    filter_condition = ""
    if request_id is not None:
        filter_condition = ""


@app.route("/request/<int:request_id>", methods=["GET"])
def get_requests_by_id(request_id):
    return str(request_id)


@app.route("/request", methods=["GET"])
def get_requests(request_id):
    return str(request_id)


@app.route("/request", methods=["POST"])
def request_book():
    if not request.json:
        abort(400)

    response = {
        "email": request.json["email"],
        "title": request.json["title"],
        "id": "",
        "timestamp": str(datetime.now()),
    }

    return response, 201

