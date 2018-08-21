
from app import app
from models import questions
from flask import jsonify

quest = questions()
@app.route("/api/v1/questions", methods =["POST"])
def createQ():
    return jsonify(quest.post_question())