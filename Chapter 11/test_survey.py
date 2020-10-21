import unittest
from Survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey"""

    def setUp(self):
        """ Create a survey and a set of responses for use in all test methods.
        """
        question = "What lang was your first language?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()
