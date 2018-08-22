from app import app
from models import questions
from flask import jsonify, request, json

quest = questions()

@app.route("/api/v1/questions", methods =["POST"])
def createQ():
    return quest.post_question()

@app.route("/api/v1/questions", methods =["GET"])
def getQ():
    return quest.get_question()

@app.route("/api/v1/questions/<int:questionId>", methods = ["GET"])
def getaQ(questionId):
    return quest.get_one_question(questionId)

@app.route("/api/v1/questions/<int:questionId>/answers", methods = ["POST"])
def createA(questionId):
    return quest.add_an_answer(questionId)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'Message': 'Page not found'}), 404

