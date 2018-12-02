# services/users/project/api/models.py


from sqlalchemy.sql import func
from project import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'active': self.active
        }

class Score(db.Model):
    'The Score model manages the score. This comment can be improved'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    turn = db.Column(db.Integer, nullable=False)
    pins = db.Column(db.Integer, nullable=False)
    cummulative_score = db.Column(db.Integer, nullable=False)
    player = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)


    def getLastTurn(self, player):
        # get the last turn number, given the player
        return ''

    def getLastScore(self, turn, player):
        # get the last score given a player
        return ''

    def getCummulative(self, turn, player):
        # get the cummulative score for the previous turn
        return ''

    def getLastPins(self, turn, player):
        # get the number of pins that were knocked down previous turn
        return ''

    def updateScore(self, turn, player, score, cummulative_score):
        # take a score model object and update the database
        return ''

    def __str__(self):
        return '%s %s' % (self.turn, self.pins, self.cummulative_score)
