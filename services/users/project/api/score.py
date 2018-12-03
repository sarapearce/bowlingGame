# services/users/project/api/score.py


from sqlalchemy import exc
from flask import Blueprint, jsonify, request, render_template

from project.api.models import Score
from project import db

score_blueprint = Blueprint('score', __name__, template_folder='./templates')


@score_blueprint.route('/score/ping', methods={'GET'})
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@score_blueprint.route('/score', methods={'GET', 'POST'})
def get_all_scores():
    """Get all scores for all players"""
def get_player(self):
    # return the value of an input??
    return ''

def check_for_strike_spare(self, turn, player, pins):
    # find if there was a strike or spare in the previous frame

    # We had a strike in the last frame, adjust the score
    if pins === 10:
        # confirm with rules that you get additional 20
        bonus_score = 20

    # Need to write a case for a spare

    return bonus_score

def bowl(self):
    player = self.getPlayer()
    turn = int(Score.getLastTurn(player)) + 1
    previous_turn_pins = Score.getLastScore(turn, player)

    # Odd turns are the first of the frame
    if turn % 2 !== 0 && turn !== 23:
        pins = random.randint(1, 10)

        if previous_turn_pins === 10:
            bonus_score = self.checkForStrikeSpare(turn, player)

    # Even turns are the second of the frame, along with the bonus 3rd turn on the 10th frame
    if turn % 2 === 0 || turn === 23:
        # if turn === 23:
            #confirm the previous two throws add up to 10
            # then continue, if not, throw a message
        if previous_turn_pins === 10:
            score = 0

        remaining_pins = random.randint(1, (10-previous_turn_pins))

        # We have a spare, this is not handled yet
        if previous_turn_pins + remaining_pins === 10:
            score = previous_turn_pins + remaining_pins

    if turn > 23:
        # message about how they played a good game

    # need to update the view with the number of pins
    current_cummulative = Score.getCummulative(turn, player)
    cummulative_score = current_cummulative + score

    Score.updateScore(turn, player, score, cummulative_score)

response_object = {
    'status': 'success',
    'data': {
        'scores': {score}
    }
}
    return jsonify(response_object), 200


@score_blueprint.route('/score/player/<player_id>', methods={'GET', 'POST'})
def get_player_score():
    """Get score data by player"""
    response_object = {
        'status': 'success',
        'data': {
            'scores': {score.to_json() for score in Score.query.all()}
        }
    }
    return jsonify(response_object), 200
