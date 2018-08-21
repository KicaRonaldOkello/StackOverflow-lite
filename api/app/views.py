
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

@app.route("/api/v1/questions/<int:questionId>")
def getaQ(questionId):
    return quest.get_one_question(questionId)

