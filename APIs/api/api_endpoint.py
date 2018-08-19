from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

QUESTION = [
    {
        "id": 1,
        "title": "What kind of questions do we ask on this patform?"
    },
    {
        "id": 2,
        "title": "How do python interpreters work?"
    },
    {
        "id": 3,
        "title": "What kind of frameworks can make web services better?"
    }
]

@app.route("/api/v1/questions", methods=["GET"])
def get_all_questions():
    """Returns all questions."""
    return jsonify({'question': QUESTION})

@app.route("/api/v1/questions/<int:questionId>", methods=["GET"])
def get_specific_question(questionId):
    """Returns specific question by Id."""
    usr = [qu for qu in QUESTION if qu["id"] == questionId]
    return jsonify({'qu': usr})

@app.route("/api/v1/questions", methods=["POST"])
def post_a_question():
    """Adds a question."""
    qun = {
        "id": request.json["id"],
        "title": request.json["title"]
    }
    QUESTION.append(qun)
    return jsonify(qun)

if __name__ == '__main__':
    app.run(debug=True)
