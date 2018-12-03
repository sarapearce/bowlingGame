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

    __tablename__ = "score"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    player = db.Column(db.String(128), nullable=False)
    turn = db.Column(db.Integer, nullable=False)
    pins = db.Column(db.Integer, default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, player, turn, pins):
        self.player = player
        self.turn = turn
        self.pins = pins

    def to_json(self):
        return {
            'id': self.id,
            'player': self.player,
            'turn': self.turn,
            'pins': self.pins
        }

    def getLastTurn(self, player):
        # get the last turn number for a given player
        lastTurnRow = db.query.filter_by(player=player).last()
        print(lastTurnRow)
        return lastTurnRow.turn

    def getLastScore(self, player):
        # get the last score for a given player
        lastTurnRow = db.query.filter_by(player=player).last()
        return lastTurnRow.cummulative_score

    def getLastPins(self, player):
        # get the number of pins that were knocked down previous turn
        lastTurnRow = db.query.filter_by(player=player).last()
        return lastTurnRow.pins

    def updateScore(self, turn, player, pins, cummulative_score):
        score = (player, turn, pins, cummulative_score)
        # take a score model object and update the database
        db.session.add(score)
        db.session.commit()
