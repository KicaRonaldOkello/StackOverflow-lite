from app import app
from flask import jsonify, json, request

QUESTION = []

class questions:
    #def __init__(self, id, title, description):
        #self.id = id = 0
        #self.title = title
        #self.description = description

    def post_question(self):
        #self.id = self.id + 1
        dat = {
        "title": request.json["title"],
        "description": request.json["description"]
    }
        QUESTION.append(dat)
        return {'question': QUESTION}


