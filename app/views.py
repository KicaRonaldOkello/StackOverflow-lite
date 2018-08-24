"""Handles all the views for the app"""
from app import app
from app.models import Questions, Answers, QUESTION, ANSWER
from flask import jsonify, request, make_response

quest = Questions()
ans = Answers()


@app.route("/api/v1/questions", methods=["POST"])
def create_q():
    """Method to add question"""
    data = {
        "title": request.json["title"],
        "description": request.json["description"]
    }
    result = [d for d in QUESTION if d['title'] == data['title']]
    if data["title"] == "":
        return make_response(jsonify({"error": "Empty question title"}), 400)
    if data["description"] == "":
        return make_response(jsonify({"Error": "Empty question body"}), 400)
    if not result:
        quest.post_question(data)
        return make_response(jsonify({'question': data}), 201)
    return make_response(jsonify({"Error": "Duplicate"}), 400)


@app.route("/api/v1/questions", methods=["GET"])
def get_q():
    """Method to get all questions."""
    if QUESTION == []:
        return make_response(jsonify({"Error": "No questions yet"}), 400)
    qns = quest.get_question()
    return make_response(jsonify({'questions': qns}), 200)


@app.route("/api/v1/questions/<int:questionId>", methods=["GET"])
def geta_Q(questionId):
    """Method to get specific question."""
    result = [k for k in QUESTION if k["id"] == questionId]
    if result:
        oneQ = quest.get_one_question(questionId)
        return make_response(jsonify({'question': oneQ}), 200)
    return make_response(jsonify({"Error": "Question does not exist"}), 404)


@app.route("/api/v1/questions/<int:questionId>/answers", methods=["POST"])
def create_a(questionId):
    """Method to add answers."""
    answer = {
        "answer": request.json["answer"]
    }
    check = [a for a in QUESTION if a["id"] == questionId]
    checkanswer = [a for a in ANSWER if a["answer"] == answer['answer']]
    if check and not checkanswer:
        ans.add_an_answer(questionId, answer)
        return make_response(jsonify({"answer": answer["answer"]}), 201)
    return make_response(jsonify({"Message": "Answer exists"}), 400)


@app.errorhandler(404)
def page_not_found(e):
    """Handles page not found errors."""
    return jsonify({'Message': 'Page not found'}), 404


@app.errorhandler(500)
def Servererror(e):
    """Handles internal server errors."""
    return jsonify({'Message': 'Internal Server Error'}), 500


@app.errorhandler(405)
def Methoderror(e):
    """Method for uncovered actions."""
    return jsonify({'Message': 'Method not supported by api'}), 405
