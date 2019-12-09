from flask import request, abort, jsonify, make_response

from src.app import app, db
from src.models import Requests, Books

from datetime import datetime


def retrieve_requests(request_id=None):
    result = None
    if request_id is not None:
        result = Requests.query.get(request_id)
    else:
        result = Requests.query.all()
    return result


@app.route("/request/<int:request_id>", methods=["GET"])
def get_requests_by_id(request_id):
    response = retrieve_requests(request_id)
    if response:
        return jsonify(response.serialize)

    abort(404)


@app.route("/request/<int:request_id>", methods=["DELETE"])
def delete_request(request_id):
    requested = retrieve_requests(request_id)
    if requested:
        db.session.delete(requested)
        db.session.commit()

        return "", 204

    abort(400)


@app.route("/request", methods=["GET"])
def get_requests():
    all_requests = retrieve_requests()
    return jsonify(
        {
            "count": len(all_requests),
            "data": [result.serialize for result in all_requests],
        }
    )


@app.route("/request", methods=["POST"])
def request_book():
    if not request.json:
        abort(400)

    email = request.json["email"]
    title = request.json["title"]

    book = Books.query.filter_by(title=title).first()

    if book:
        new_record = Requests(email=email, book_id=book.id)
        db.session.add(new_record)
        db.session.commit()
        response = {
            "email": new_record.email,
            "title": book.title,
            "id": new_record.id,
            "timestamp": new_record.created_on,
        }

        return response, 201
    else:
        return make_response(
            jsonify({"status": "error", "message": "Cannot find title"}), 400
        )


@app.route("/")
def hello():
    return "Hello!"
