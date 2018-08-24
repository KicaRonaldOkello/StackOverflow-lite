"""Handles all the data manipulation."""

QUESTION = []
ANSWER = []


class Questions:
    """Class to handle question actions."""

    def post_question(self, data):
        """Method to questions."""
        data["id"] = (len(QUESTION) + 1)
        QUESTION.append(data)
        return data

    def get_question(self):
        """Method to return all questions."""
        return QUESTION

    def get_one_question(self, questionId):
        """Method to return one question."""
        return QUESTION[questionId == "id"]["title"]


class Answers:
    """Class to handle answer actions."""

    def add_an_answer(self, questionId, answer):
        """Method to add answers."""
        answer["Q_id"] = questionId
        answer["A_id"] = (len(ANSWER) + 1)
        ANSWER.append(answer)
