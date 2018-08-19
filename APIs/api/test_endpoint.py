import unittest
from api_endpoint import app
import json


class TestAllApiEndPoints(unittest.TestCase):
    """Class for all unittests."""
    def setUp(self):
        """Initialising test conditions."""
        self.client = app.test_client()

    def test_get_all_questions(self):
        """Test method that fetches all questons."""
        response = self.client.get("http://localhost:5000/api/v1/questions")
        self.assertEquals(response.status_code, 200)

    def test_get_specific_question(self):
        """Test method that fetches specific question."""
        response = self.client.get("http://localhost:5000/api/v1/questions/1")
        self.assertEquals(response.status_code, 200)

    def test_post_a_question(self):
        """Test method that posts a question"""
        sample = {"id": 9, "title": "How do endpoints work?"}
        response = self.client.post("http://localhost:5000/api/v1/questions",
                                    data = json.dumps(sample),
                                    content_type = 'application/json')
        self.assertAlmostEquals(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
