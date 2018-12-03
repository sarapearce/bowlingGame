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
    response_object = {
        'status': 'success',
        'data': {
            'scores': {score.to_json() for score in Score.query.all()}
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
