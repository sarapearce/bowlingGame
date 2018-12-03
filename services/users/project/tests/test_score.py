# services/users/project/tests/test_score.py
import json
import unittest

from project import db
from project.api.models import Score
from project.tests.base import BaseTestCase


def add_turn(turn, pins):
    # Add a bowling turn to our test player.
    score = Score(turn=turn, pins=pins, player='test')
    db.session.add(score)
    db.session.commit()
    return score

class ScoreModelTests(BaseTestCase):
    """Tests for the Score Service."""

    def test_score_ping(self):
        """Ensure the /ping route behaves correctly."""
        response = self.client.get('/score/ping')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])

    def test_add_turn(self):
        """Ensure a new score can be added to the database."""
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': 'test',
                    'turn': 3,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])


    def the_second_score_should_be_within_remaining_pins(self):
        """
        Some comment that further elaborates what we are testing
        """
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': '1',
                    'turn': 4,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertEqual()



    def pins_should_return_a_value_less_than_11(self):
        """
        Some comment that further elaborates what we are testing
        """
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': 'test',
                    'turn': 4,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertEqual()


    def cummulative_score_should_be_cummulative(self):
        """
        Some comment that further elaborates what we are testing
        """
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': 'test',
                    'turn': 4,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertEqual()


    def previous_scores_should_be_for_correct_player(self):
        """
        Some comment that further elaborates what we are testing
        """
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': 'test',
                    'turn': 4,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertEqual()


    def strike_score_should_add_correctly(self):
        """
        Some comment that further elaborates what we are testing
        """
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': 'test',
                    'turn': 4,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertEqual()


    def spare_score_should_add_correctly(self):
        """
        Some comment that further elaborates what we are testing
        """
        with self.client:
            response = self.client.post(
                '/score',
                data=json.dumps({
                    'player': 'test',
                    'turn': 4,
                    'pins' : 7
                }),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertIn('success', data['status'])
            self.assertEqual()


if __name__ == '__main__':
    unittest.main()
