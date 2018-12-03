# services/users/project/api/users.py


from sqlalchemy import exc
from flask import Blueprint, jsonify, request, render_template

from project.api.models import User
from project import db

users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/users/ping', methods={'GET'})
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@users_blueprint.route('/users', methods={'GET', 'POST'})
def get_all_users():
    """Get all users"""
    response_object = {
        'status': 'success',
        'data': {
            'users': {user.to_json() for user in User.query.all()}
        }
    }
    return jsonify(response_object), 200
