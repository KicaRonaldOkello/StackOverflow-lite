
from app import app
from models import questions
from flask import jsonify, request, json

quest = questions()

@app.route("/api/v1/questions", methods =["POST"])
def createQ():
    
    return quest.post_question()
