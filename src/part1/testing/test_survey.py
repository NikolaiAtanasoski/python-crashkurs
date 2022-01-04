import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "Which pokemon do you think is the best?"
        self.pokemon_survey = AnonymousSurvey(question)
        self.responses = ["Schiggy", "Bisasam", "Porenta"]

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.pokemon_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.pokemon_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.pokemon_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.pokemon_survey.responses)


if __name__ == "__main__":
    unittest.main()
