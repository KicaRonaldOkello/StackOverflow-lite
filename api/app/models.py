from app import app
from flask import jsonify, request, json, make_response

QUESTION = []
ANSWER = []

class questions:

    def post_question(self): 
        data = {
            "id": len(QUESTION) + 1,
            "title": request.json["title"],
            "description": request.json["description"]
    }
        if data["title"]== "":
            return make_response(jsonify({"error": "Empty question title"}), 400)
        if data["description"] == "":
            return make_response(jsonify({"Error": "Empty question body"}), 400)
        else:
            QUESTION.append(data)
            return make_response(jsonify({'question': data}), 201)

    def get_question(self):
        if QUESTION == []:
            return make_response(jsonify({"Error": "No questions yet"}), 400)
        else:
            return make_response(jsonify({'questions': QUESTION}), 200)

    def get_one_question(self, questionId):
        oneQ = [k for k in QUESTION if k["id"] == questionId]
        if oneQ:
            return make_response(jsonify({'question': oneQ}), 200)
        else:
            return make_response(jsonify({"Error": "Question does not exist"}), 404)
        

    def add_an_answer(self, questionId):
        answer = {
            "Q_id": questionId,
            "A_id": len(ANSWER) + 1,
            "answer": request.json["answer"]
        }
        check = [a for a in QUESTION if a["id"] == questionId]
        if check:
            ANSWER.append(answer)
            return make_response(jsonify({"answer": ANSWER}), 201)




