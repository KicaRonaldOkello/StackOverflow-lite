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
            return make_response(jsonify({"error": "Empty question title"}), 204)
        if data["description"] == "":
            return make_response(jsonify({"Error": "Empty question body"}), 204)
        else:
            QUESTION.append(data)
            return make_response(jsonify({'question': data}), 201)

    def get_question(self):
        return make_response(jsonify({'questions': QUESTION}), 200)

    def get_one_question(self, questionId):
        if type(questionId) == int:
            if questionId <= len(QUESTION):
                oneQ = [k for k in QUESTION if k["id"] == questionId]
                return make_response(jsonify({'question': oneQ}), 200)
            else:
                return make_response(jsonify({"Error": "Question does not exist"}), 204)
        if type(questionId) == chr:
            return make_response(jsonify({"Error": "Wrong question id. Use integer"}), 405)



