from flask import Flask
from flask import jsonify

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

if __name__ == '__main__':
    app.run(debug=True)
