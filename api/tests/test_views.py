import unittest
from api.app import app
import json

class TestEndpoint(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_question(self):
        sample = {
            "id": 2,
            "title": "how to test?",
            "description": "briefly explain unittesting"
        }
        response = self.client.post("/api/v1/questions", data = json.dumps(sample), content_type= 'application/json')
        self.assertEqual(response.status_code, 201)

    def test_get_questions(self):
        response = self.client.get("/api/v1/questions")
        self.assertEqual(response.status_code, 200)

    def test_get_one_question(self):
        sample2 = {
            "id": 1,
            "title": "Test data",
            "description": "How do you do unittest?"
        }
        self.client.post("/api/v1/questons", data = json.dumps(sample2), content_type = 'application/json')
        response = self.client.get("/api/v1/questions/1")
        self.assertEqual(response.status_code, 200)

    def test_post_answer(self):
        test_data = {
            "id": 1,
            "title": "Trial data",
            "description": "How do you do unittest?"
        }
        self.client.post("/api/v1/questons", data = json.dumps(test_data), content_type = 'application/json')
        ans_data = {
            "Q_id": 1,
            "A_id": 1,
            "answer": "This is the answer"
        }
        response = self.client.post("/api/v1/questions/1/answers", data = json.dumps(ans_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()