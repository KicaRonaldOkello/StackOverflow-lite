from app import app
from flask import jsonify, request, json, make_response

QUESTION = []

class questions:

    def post_question(self): 
        data = {
            "id": len(QUESTION) + 1,
            "title": request.json["title"],
            "description": request.json["description"]
    }
        if data["title"]== "":
            return make_response(jsonify({"error": "Empty question title"}), 404)
        if data["description"] == "":
            return make_response(jsonify({"Error": "Empty question body"}), 404)
        else:
            QUESTION.append(data)
            return make_response(jsonify({'question': QUESTION}), 201)



