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
        response = self.client.get("http://localhost:5000/api/v1/questions")
        self.assertEquals(response.status_code, 200)



if __name__ == '__main__':
    unittest.main()
