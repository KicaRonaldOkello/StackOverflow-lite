import unittest
import json
from api_endpoint import app



class TestAllApiEndPoints(unittest.TestCase):
    """Class for all unittests."""
    def setUp(self):
        """Initialising test conditions."""
        self.client = app.test_client()

    def test_get_all_questions(self):
        """Test method that fetches all questons."""
        response = self.client.get("/api/v1/questions")
        self.assertEquals(response.status_code, 200)

    def test_get_specific_question(self):
        """Test method that fetches specific question."""
        response = self.client.get("/api/v1/questions/1")
        self.assertEquals(response.status_code, 200)

    def test_post_a_question(self):
        """Test method that posts a question"""
        sample = {"id": 9, "title": "How do endpoints work?"}
        response = self.client.post("/api/v1/questions",
                                    data = json.dumps(sample),
                                    content_type = 'application/json')
        self.assertEquals(response.status_code, 200)

    def test_add_answer_to_question(self):
        """Test method to add answers."""
        sample_answer = {"id": 10, "ans": "this is correct"}
        response = self.client.post("/api/v1/questions/3/answers",
                                    data = json.dumps(sample_answer),
                                    content_type = 'application/json')
        self.assertEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
