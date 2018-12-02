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

class Sizing(db.Model):

    __tablename__ = "sizing"

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    motor = db.Column(db.String(128), nullable=False)
    control = db.Column(db.String(128), nullable=False)
    plunger = db.Column(db.String(128), nullable=False)
    head = db.Column(db.String(128), nullable=False)
    pressure = db.Column(db.String(128), nullable=False)
    minimumspeed = db.Column(db.String(128), nullable=False)
    flowminccpermin = db.Column(db.String(128), nullable=False)
    ahmin = db.Column(db.String(128), nullable=False)
    flowmaxccpermin = db.Column(db.String(128), nullable=False)
    ahmax = db.Column(db.String(128), nullable=False)
    slope = db.Column(db.String(128), nullable=False)
    yintercept = db.Column(db.String(128), nullable=False)
    flowmingpd = db.Column(db.String(128), nullable=False)
    flowmaxgpd = db.Column(db.String(128), nullable=False)
    flowmingpdup5 = db.Column(db.String(128), nullable=False)

    def __init__(self, motor, control, plunger, head, pressure, minimumspeed, flowminccpermin,
    ahmin, flowmaxccpermin, ahmax, slope, yintercept, flowmingpd, flowmaxgpd, flowmingpdup5):
        self.motor = motor
        self.control = control
        self.plunger = plunger
        self.head = head
        self.pressure = pressure
        self.minimumspeed = minimumspeed
        self.flowminccpermin = flowminccpermin
        self.ahmin = ahmin
        self.flowmaxccpermin = flowmaxccpermin
        self.ahmax = ahmax
        self.slope = slope
        self.yintercept = yintercept
        self.flowmingpd = flowmingpd
        self.flowmaxgpd = flowmaxgpd
        self.flowmingpdup5 = flowmingpdup5

    def to_json(self):
        return {
            'id': self.id,
            'motor': self.motor,
            'control': self.control,
            'plunger': self.plunger,
            'head': self.head,
            'pressure': self.pressure,
            'minimumspeed': self.minimumspeed,
            'flowminccpermin': self.flowminccpermin,
            'ahmin': self.ahmin,
            'flowmaxccpermin': self.flowmaxccpermin,
            'ahmax': self.ahmax,
            'slope': self.slope,
            'yintercept': self.yintercept,
            'flowmingpd': self.flowmingpd,
            'flowmaxgpd': self.flowmaxgpd,
            'flowmingpdup5': self.flowmingpdup5
        }

# class SmSizing(db.Model):
#
#     __tablename__ = "smsizing"
#
#     id = db.Column(db.Integer, primary_key=True, autoincrement=False)
#     motor = db.Column(db.String(128), nullable=False)
#     control = db.Column(db.String(128), nullable=False)
#     plunger = db.Column(db.String(128), nullable=False)
#     head = db.Column(db.String(128), nullable=False)
#     pressure = db.Column(db.String(128), nullable=False)
#     minimumspeed = db.Column(db.String(128), nullable=False)
#     flowminccpermin = db.Column(db.String(128), nullable=False)
#     ahmin = db.Column(db.String(128), nullable=False)
#     flowmaxccpermin = db.Column(db.String(128), nullable=False)
#     ahmax = db.Column(db.String(128), nullable=False)
#     slope = db.Column(db.String(128), nullable=False)
#     yintercept = db.Column(db.String(128), nullable=False)
#     flowmingpd = db.Column(db.String(128), nullable=False)
#     flowmaxgpd = db.Column(db.String(128), nullable=False)
#     flowmingpdup5 = db.Column(db.String(128), nullable=False)
#
#     def __init__(self, motor, control, plunger, head, pressure, minimumspeed, flowminccpermin,
#     ahmin, flowmaxccpermin, ahmax, slope, yintercept, flowmingpd, flowmaxgpd, flowmingpdup5):
#         self.motor = motor
#         self.control = control
#         self.plunger = plunger
#         self.head = head
#         self.pressure = pressure
#         self.minimumspeed = minimumspeed
#         self.flowminccpermin = flowminccpermin
#         self.ahmin = ahmin
#         self.flowmaxccpermin = flowmaxccpermin
#         self.ahmax = ahmax
#         self.slope = slope
#         self.yintercept = yintercept
#         self.flowmingpd = flowmingpd
#         self.flowmaxgpd = flowmaxgpd
#         self.flowmingpdup5 = flowmingpdup5
#
#     def to_json(self):
#         return {
#             'id': self.id,
#             'motor': self.motor,
#             'control': self.control,
#             'plunger': self.plunger,
#             'head': self.head,
#             'pressure': self.pressure,
#             'minimumspeed': self.minimumspeed,
#             'flowminccpermin': self.flowminccpermin,
#             'ahmin': self.ahmin,
#             'flowmaxccpermin': self.flowmaxccpermin,
#             'ahmax': self.ahmax,
#             'slope': self.slope,
#             'yintercept': self.yintercept,
#             'flowmingpd': self.flowmingpd,
#             'flowmaxgpd': self.flowmaxgpd,
#             'flowmingpdup5': self.flowmingpdup5
#         }
