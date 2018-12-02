# services/users/project/api/users.py


from sqlalchemy import exc
from flask import Blueprint, jsonify, request, render_template

from project.api.models import User
from project.api.models import Sizing
# from project.api.models import SmSizing
from project import db

users_blueprint = Blueprint('users', __name__, template_folder='./templates')


@users_blueprint.route('/users/ping', methods={'GET'})
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })


@users_blueprint.route('/users', methods={'GET'})
def get_all_users():
    """Get all users"""
    response_object = {
        'status': 'success',
        'data': {
            'users': {user.to_json() for user in User.query.all()}
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/motors', methods={'GET'})
def get_motor_data():
    """Get motor data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': ['12G', '12E', '12X']
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/controls', methods={'GET'})
def get_controls_data():
    """Get controls data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': [
                'Cont. Run',
                'On/Off',
                'Low Flow'
            ]
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/heads', methods={'GET'})
def get_head_data():
    """Get head data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': [
                'Dual',
                'Single'
            ]
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/panels', methods={'GET'})
def get_panel_data():
    """Get panel data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': {
                '60': 3.0,
                '85': 5.0,
                '140': 8.0,
                '150': 8.56,
            }
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/plungers', methods={'GET'})
def get_plunger_data():
    """Get plunger data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': {
                '3/16': 0.18,
                '1/4': 0.25,
                '3/8': 0.37,
                '1/2': 0.50,
            }
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/pressure', methods={'GET'})
def get_pressure_data():
    """Get pressure data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': [
                0,
                250,
                500,
                750,
                1000,
                1250,
                1500,
                1750,
                2000,
                2250,
                2500,
                2750,
                3000,
                3250,
                3500,
                3750,
                4000,
                4250,
                4500,
                4750,
                5000,
                5250,
                5500,
                5750,
                6000
            ]
        }
    }
    return jsonify(response_object), 200


@users_blueprint.route('/users/smsizing', methods={'GET'})
def get_smallset_data():
    """Get a small subset of sizing table data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': [sizing.to_json() for sizing in Sizing.query.limit(10)]
        }
    }
    return jsonify(response_object), 200

@users_blueprint.route('/users/sizing', methods={'GET'})
def get_all_data():
    """Get all sizing table data"""
    response_object = {
        'status': 'success',
        'data': {
            'types': [sizing.to_json() for sizing in Sizing.query.all()]
        }
    }
    return jsonify(response_object), 200

# @users_blueprint.route('/users/smsizing', methods={'GET'})
# def get_all_data():
#     """Get a small set from the sizing table while we wait"""
#     response_object = {
#         'status': 'success',
#         'data': {
#             'types': [smsizing.to_json() for smsizing in SmSizing.query.all()]
#         }
#     }
#     return jsonify(response_object), 200


@users_blueprint.route('/users/locations', methods={'GET'})
def get_location_data():
    """Get Location data"""
    response_object = {
        'status': 'success',
        'data': {
            'types':
            [
                {
                    'State': 'Tx',
                    'City': 'Kenedy',
                    'SunlightMin': '3.83',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Kenedy',
                    'Latitude': '28.81',
                    'Longitude': '-97.84',
                    'Declination': '4',
                    'TiltAngle': '25.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Pa',
                    'City': 'Bridgeville',
                    'SunlightMin': '2.34',
                    'SunlightAvg': '4.00',
                    'Location': 'Pa - Bridgeville',
                    'Latitude': '40.35',
                    'Longitude': '-80.11',
                    'Declination': '9',
                    'TiltAngle': '34.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'La',
                    'City': 'Alexandria',
                    'SunlightMin': '4.53',
                    'SunlightAvg': '6.00',
                    'Location': 'La - Alexandria',
                    'Latitude': '34.04',
                    'Longitude': '-118.25',
                    'Declination': '12',
                    'TiltAngle': '29.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Amarillo',
                    'SunlightMin': '4.75',
                    'SunlightAvg': '6.00',
                    'Location': 'Tx - Amarillo',
                    'Latitude': '35.20',
                    'Longitude': '-101.79',
                    'Declination': '7',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Austin',
                    'SunlightMin': '3.97',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Austin',
                    'Latitude': '30.23',
                    'Longitude': '-97.93',
                    'Declination': '4',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Nd',
                    'City': 'Bismarck',
                    'SunlightMin': '2.46',
                    'SunlightAvg': '5.00',
                    'Location': 'Nd - Bismarck',
                    'Latitude': '46.82',
                    'Longitude': '-100.85',
                    'Declination': '6',
                    'TiltAngle': '39.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Boerne',
                    'SunlightMin': '4.00',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Boerne',
                    'Latitude': '29.82',
                    'Longitude': '-98.69',
                    'Declination': '5',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ca',
                    'City': 'Bakersfield',
                    'SunlightMin': '3.18',
                    'SunlightAvg': '6.00',
                    'Location': 'Ca - Bakersfield',
                    'Latitude': '35.37',
                    'Longitude': '-119.00',
                    'Declination': '13',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Nv',
                    'City': 'Ely',
                    'SunlightMin': '4.15',
                    'SunlightAvg': '6.00',
                    'Location': 'Nv - Ely',
                    'Latitude': '39.00',
                    'Longitude': '-114.00',
                    'Declination': '13',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Can',
                    'City': 'Calgary',
                    'SunlightMin': '1.97',
                    'SunlightAvg': '4.00',
                    'Location': 'Can - Calgary',
                    'Latitude': '51.04',
                    'Longitude': '-114.05',
                    'Declination': '15',
                    'TiltAngle': '42.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Carrizo Springs',
                    'SunlightMin': '4.15',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Carrizo Springs',
                    'Latitude': '28.52',
                    'Longitude': '-99.86',
                    'Declination': '5',
                    'TiltAngle': '25.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Wy',
                    'City': 'Casper',
                    'SunlightMin': '3.90',
                    'SunlightAvg': '6.00',
                    'Location': 'Wy - Casper',
                    'Latitude': '42.86',
                    'Longitude': '-106.31',
                    'Declination': '10',
                    'TiltAngle': '36.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Wy',
                    'City': 'Cheyenne',
                    'SunlightMin': '4.44',
                    'SunlightAvg': '6.00',
                    'Location': 'Wy - Cheyenne',
                    'Latitude': '41.13',
                    'Longitude': '-104.82',
                    'Declination': '9',
                    'TiltAngle': '34.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Dallas',
                    'SunlightMin': '4.06',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Dallas',
                    'Latitude': '32.78',
                    'Longitude': '-96.80',
                    'Declination': '4',
                    'TiltAngle': '28.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Co',
                    'City': 'Denver',
                    'SunlightMin': '4.61',
                    'SunlightAvg': '6.00',
                    'Location': 'Co - Denver',
                    'Latitude': '39.73',
                    'Longitude': '-104.98',
                    'Declination': '9',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'El Paso',
                    'SunlightMin': '5.44',
                    'SunlightAvg': '7.00',
                    'Location': 'Tx - El Paso',
                    'Latitude': '31.75',
                    'Longitude': '-106.48',
                    'Declination': '9',
                    'TiltAngle': '27.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ok',
                    'City': 'Elk City',
                    'SunlightMin': '4.35',
                    'SunlightAvg': '6.00',
                    'Location': 'Ok - Elk City',
                    'Latitude': '35.41',
                    'Longitude': '-99.40',
                    'Declination': '5',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'ND',
                    'City': 'Fargo',
                    'SunlightMin': '2.12',
                    'SunlightAvg': '4.00',
                    'Location': 'ND - Fargo',
                    'Latitude': '46.87',
                    'Longitude': '-96.78',
                    'Declination': '3',
                    'TiltAngle': '39.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Co',
                    'City': 'Grand Junction',
                    'SunlightMin': '4.41',
                    'SunlightAvg': '6.00',
                    'Location': 'Co - Grand Junction',
                    'Latitude': '39.06',
                    'Longitude': '-108.55',
                    'Declination': '10',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Houston',
                    'SunlightMin': '3.69',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Houston',
                    'Latitude': '29.76',
                    'Longitude': '-95.36',
                    'Declination': '3',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Longview',
                    'SunlightMin': '3.76',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Longview',
                    'Latitude': '32.50',
                    'Longitude': '-94.74',
                    'Declination': '2',
                    'TiltAngle': '28.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'ND',
                    'City': 'Minot',
                    'SunlightMin': '2.26',
                    'SunlightAvg': '4.00',
                    'Location': 'ND - Minot',
                    'Latitude': '48.23',
                    'Longitude': '-101.29',
                    'Declination': '7',
                    'TiltAngle': '40.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'OK',
                    'City': 'Oklahoma City',
                    'SunlightMin': '4.13',
                    'SunlightAvg': '5.00',
                    'Location': 'OK - Oklahoma City',
                    'Latitude': '35.46',
                    'Longitude': '-97.51',
                    'Declination': '4',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Pa',
                    'City': 'Philadelphia',
                    'SunlightMin': '3.34',
                    'SunlightAvg': '5.00',
                    'Location': 'Pa - Philadelphia',
                    'Latitude': '39.95',
                    'Longitude': '-75.16',
                    'Declination': '12',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Pa',
                    'City': 'Pittsburgh',
                    'SunlightMin': '2.26',
                    'SunlightAvg': '4.00',
                    'Location': 'Pa - Pittsburgh',
                    'Latitude': '40.44',
                    'Longitude': '-79.99',
                    'Declination': '9',
                    'TiltAngle': '34.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'La',
                    'City': 'Shreveport',
                    'SunlightMin': '3.70',
                    'SunlightAvg': '5.00',
                    'Location': 'La - Shreveport',
                    'Latitude': '32.52',
                    'Longitude': '-93.75',
                    'Declination': '2',
                    'TiltAngle': '28.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ok',
                    'City': 'Tulsa',
                    'SunlightMin': '3.89',
                    'SunlightAvg': '5.00',
                    'Location': 'Ok - Tulsa',
                    'Latitude': '36.15',
                    'Longitude': '-95.99',
                    'Declination': '3',
                    'TiltAngle': '31.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ut',
                    'City': 'Vernal',
                    'SunlightMin': '3.79',
                    'SunlightAvg': '6.00',
                    'Location': 'Ut - Vernal',
                    'Latitude': '40.45',
                    'Longitude': '-109.52',
                    'Declination': '11',
                    'TiltAngle': '34.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ks',
                    'City': 'Wichita',
                    'SunlightMin': '4.01',
                    'SunlightAvg': '5.00',
                    'Location': 'Ks - Wichita',
                    'Latitude': '37.68',
                    'Longitude': '-97.33',
                    'Declination': '4',
                    'TiltAngle': '32.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Wv',
                    'City': 'Bridgeport',
                    'SunlightMin': '2.58',
                    'SunlightAvg': '4.00',
                    'Location': 'Wv - Bridgeport',
                    'Latitude': '39.28',
                    'Longitude': '-80.25',
                    'Declination': '9',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'La',
                    'City': 'Houma',
                    'SunlightMin': '4.12',
                    'SunlightAvg': '5.00',
                    'Location': 'La - Houma',
                    'Latitude': '29.59',
                    'Longitude': '-90.71',
                    'Declination': '0',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'Bryan',
                    'SunlightMin': '3.82',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - Bryan',
                    'Latitude': '30.67',
                    'Longitude': '-96.36',
                    'Declination': '3',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'TX',
                    'City': 'Odessa',
                    'SunlightMin': '5.03',
                    'SunlightAvg': '6.00',
                    'Location': 'TX - Odessa',
                    'Latitude': '31.84',
                    'Longitude': '-102.36',
                    'Declination': '7',
                    'TiltAngle': '27.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ny',
                    'City': 'New York',
                    'SunlightMin': '3.17',
                    'SunlightAvg': '4.00',
                    'Location': 'Ny - New York',
                    'Latitude': '40.71',
                    'Longitude': '-74.01',
                    'Declination': '13',
                    'TiltAngle': '34.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Ca',
                    'City': 'San Francisco',
                    'SunlightMin': '3.25',
                    'SunlightAvg': '5.00',
                    'Location': 'Ca - San Francisco',
                    'Latitude': '37.77',
                    'Longitude': '-122.41',
                    'Declination': '14',
                    'TiltAngle': '32.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Il',
                    'City': 'Chicago',
                    'SunlightMin': '2.62',
                    'SunlightAvg': '4.00',
                    'Location': 'Il - Chicago',
                    'Latitude': '41.87',
                    'Longitude': '-87.62',
                    'Declination': '4',
                    'TiltAngle': '35.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Nv',
                    'City': 'Las Vegas',
                    'SunlightMin': '5.15',
                    'SunlightAvg': '6.00',
                    'Location': 'Nv - Las Vegas',
                    'Latitude': '36.11',
                    'Longitude': '-115.17',
                    'Declination': '12',
                    'TiltAngle': '31.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Fl',
                    'City': 'Orlando',
                    'SunlightMin': '4.34',
                    'SunlightAvg': '5.00',
                    'Location': 'Fl - Orlando',
                    'Latitude': '28.53',
                    'Longitude': '-81.37',
                    'Declination': '6',
                    'TiltAngle': '25.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'DC',
                    'City': 'Washington, D. C.',
                    'SunlightMin': '3.57',
                    'SunlightAvg': '5.00',
                    'Location': 'DC - Washington, D. C.',
                    'Latitude': '38.91',
                    'Longitude': '-77.04',
                    'Declination': '11',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Ma',
                    'City': 'Boston',
                    'SunlightMin': '2.92',
                    'SunlightAvg': '4.00',
                    'Location': 'Ma - Boston',
                    'Latitude': '42.36',
                    'Longitude': '-71.06',
                    'Declination': '15',
                    'TiltAngle': '35.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Ca',
                    'City': 'Los Angeles',
                    'SunlightMin': '4.53',
                    'SunlightAvg': '6.00',
                    'Location': 'Ca - Los Angeles',
                    'Latitude': '34.05',
                    'Longitude': '-118.24',
                    'Declination': '12',
                    'TiltAngle': '29.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Hi',
                    'City': 'Honolulu',
                    'SunlightMin': '5.06',
                    'SunlightAvg': '6.00',
                    'Location': 'Hi - Honolulu',
                    'Latitude': '21.31',
                    'Longitude': '-157.86',
                    'Declination': '10',
                    'TiltAngle': '19.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'La',
                    'City': 'New Orleans',
                    'SunlightMin': '4.03',
                    'SunlightAvg': '5.00',
                    'Location': 'La - New Orleans',
                    'Latitude': '29.95',
                    'Longitude': '-90.07',
                    'Declination': '0',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Wa',
                    'City': 'Seatle',
                    'SunlightMin': '1.49',
                    'SunlightAvg': '4.00',
                    'Location': 'Wa - Seatle',
                    'Latitude': '47.61',
                    'Longitude': '-122.33',
                    'Declination': '16',
                    'TiltAngle': '39.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Fl',
                    'City': 'Miami',
                    'SunlightMin': '4.58',
                    'SunlightAvg': '5.00',
                    'Location': 'Fl - Miami',
                    'Latitude': '25.79',
                    'Longitude': '-80.27',
                    'Declination': '6',
                    'TiltAngle': '23.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Az',
                    'City': 'Sedona',
                    'SunlightMin': '5.15',
                    'SunlightAvg': '6.00',
                    'Location': 'Az - Sedona',
                    'Latitude': '34.87',
                    'Longitude': '-111.76',
                    'Declination': '11',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ga',
                    'City': 'Savannah',
                    'SunlightMin': '4.14',
                    'SunlightAvg': '5.00',
                    'Location': 'Ga - Savannah',
                    'Latitude': '32.08',
                    'Longitude': '-81.10',
                    'Declination': '7',
                    'TiltAngle': '27.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'SC',
                    'City': 'Charleston',
                    'SunlightMin': '4.07',
                    'SunlightAvg': '5.00',
                    'Location': 'SC - Charleston',
                    'Latitude': '32.78',
                    'Longitude': '-79.93',
                    'Declination': '8',
                    'TiltAngle': '28.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Ca',
                    'City': 'Napa',
                    'SunlightMin': '3.01',
                    'SunlightAvg': '5.00',
                    'Location': 'Ca - Napa',
                    'Latitude': '38.30',
                    'Longitude': '-122.29',
                    'Declination': '14',
                    'TiltAngle': '32.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Tx',
                    'City': 'San Antonio',
                    'SunlightMin': '3.96',
                    'SunlightAvg': '5.00',
                    'Location': 'Tx - San Antonio',
                    'Latitude': '29.42',
                    'Longitude': '-98.49',
                    'Declination': '5',
                    'TiltAngle': '25.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Or',
                    'City': 'Portland',
                    'SunlightMin': '1.81',
                    'SunlightAvg': '4.00',
                    'Location': 'Or - Portland',
                    'Latitude': '45.52',
                    'Longitude': '-122.68',
                    'Declination': '16',
                    'TiltAngle': '38.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'SC',
                    'City': 'Myrtle Beach',
                    'SunlightMin': '3.89',
                    'SunlightAvg': '5.00',
                    'Location': 'SC - Myrtle Beach',
                    'Latitude': '33.69',
                    'Longitude': '-78.89',
                    'Declination': '9',
                    'TiltAngle': '29.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Ca',
                    'City': 'Palm Springs',
                    'SunlightMin': '5.04',
                    'SunlightAvg': '6.00',
                    'Location': 'Ca - Palm Springs',
                    'Latitude': '33.83',
                    'Longitude': '-116.55',
                    'Declination': '12',
                    'TiltAngle': '29.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Fl',
                    'City': 'Naples',
                    'SunlightMin': '4.76',
                    'SunlightAvg': '5.00',
                    'Location': 'Fl - Naples',
                    'Latitude': '26.14',
                    'Longitude': '-81.79',
                    'Declination': '5',
                    'TiltAngle': '23.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Az',
                    'City': 'Phoenix',
                    'SunlightMin': '5.37',
                    'SunlightAvg': '6.00',
                    'Location': 'Az - Phoenix',
                    'Latitude': '33.45',
                    'Longitude': '-112.07',
                    'Declination': '11',
                    'TiltAngle': '29.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Ca',
                    'City': 'San Diego',
                    'SunlightMin': '5.03',
                    'SunlightAvg': '6.00',
                    'Location': 'Ca - San Diego',
                    'Latitude': '32.72',
                    'Longitude': '-117.16',
                    'Declination': '12',
                    'TiltAngle': '28.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Mi',
                    'City': 'Detroit',
                    'SunlightMin': '1.90',
                    'SunlightAvg': '4.00',
                    'Location': 'Mi - Detroit',
                    'Latitude': '42.33',
                    'Longitude': '-83.05',
                    'Declination': '7',
                    'TiltAngle': '35.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Fl',
                    'City': 'Jacksonville',
                    'SunlightMin': '4.14',
                    'SunlightAvg': '5.00',
                    'Location': 'Fl - Jacksonville',
                    'Latitude': '30.33',
                    'Longitude': '-81.66',
                    'Declination': '6',
                    'TiltAngle': '26.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Oh',
                    'City': 'Columbus',
                    'SunlightMin': '2.25',
                    'SunlightAvg': '4.00',
                    'Location': 'Oh - Columbus',
                    'Latitude': '39.96',
                    'Longitude': '-83.00',
                    'Declination': '7',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Tn',
                    'City': 'Memphis',
                    'SunlightMin': '3.36',
                    'SunlightAvg': '5.00',
                    'Location': 'Tn - Memphis',
                    'Latitude': '35.15',
                    'Longitude': '-90.05',
                    'Declination': '1',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Md',
                    'City': 'Baltimore',
                    'SunlightMin': '3.43',
                    'SunlightAvg': '5.00',
                    'Location': 'Md - Baltimore',
                    'Latitude': '39.29',
                    'Longitude': '-76.61',
                    'Declination': '11',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Wi',
                    'City': 'Milwaukee',
                    'SunlightMin': '2.69',
                    'SunlightAvg': '4.00',
                    'Location': 'Wi - Milwaukee',
                    'Latitude': '43.04',
                    'Longitude': '-87.91',
                    'Declination': '4',
                    'TiltAngle': '36.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Az',
                    'City': 'Tucson',
                    'SunlightMin': '5.59',
                    'SunlightAvg': '6.00',
                    'Location': 'Az - Tucson',
                    'Latitude': '32.22',
                    'Longitude': '-110.93',
                    'Declination': '10',
                    'TiltAngle': '28.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'NM',
                    'City': 'Albuquerque',
                    'SunlightMin': '5.27',
                    'SunlightAvg': '6.00',
                    'Location': 'NM - Albuquerque',
                    'Latitude': '35.11',
                    'Longitude': '-106.61',
                    'Declination': '9',
                    'TiltAngle': '30.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Mo',
                    'City': 'Kansas City',
                    'SunlightMin': '3.61',
                    'SunlightAvg': '5.00',
                    'Location': 'Mo - Kansas City',
                    'Latitude': '39.10',
                    'Longitude': '-94.58',
                    'Declination': '2',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Oh',
                    'City': 'Cleveland',
                    'SunlightMin': '2.16',
                    'SunlightAvg': '4.00',
                    'Location': 'Oh - Cleveland',
                    'Latitude': '41.50',
                    'Longitude': '-81.70',
                    'Declination': '8',
                    'TiltAngle': '35.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Va',
                    'City': 'Virginia Beach',
                    'SunlightMin': '3.59',
                    'SunlightAvg': '5.00',
                    'Location': 'Va - Virginia Beach',
                    'Latitude': '36.85',
                    'Longitude': '-75.98',
                    'Declination': '11',
                    'TiltAngle': '31.00',
                    'DeclinationDirection': '2',
                },
                {
                    'State': 'Ne',
                    'City': 'Omaha',
                    'SunlightMin': '3.17',
                    'SunlightAvg': '5.00',
                    'Location': 'Ne - Omaha',
                    'Latitude': '41.25',
                    'Longitude': '-96.00',
                    'Declination': '3',
                    'TiltAngle': '34.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Co',
                    'City': 'Colorado Springs',
                    'SunlightMin': '4.91',
                    'SunlightAvg': '6.00',
                    'Location': 'Co - Colorado Springs',
                    'Latitude': '38.83',
                    'Longitude': '-104.82',
                    'Declination': '8',
                    'TiltAngle': '33.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Mn',
                    'City': 'Minneapolis',
                    'SunlightMin': '2.85',
                    'SunlightAvg': '4.00',
                    'Location': 'Mn - Minneapolis',
                    'Latitude': '44.98',
                    'Longitude': '-93.27',
                    'Declination': '0',
                    'TiltAngle': '37.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Can',
                    'City': 'Whitecourt',
                    'SunlightMin': '1.21',
                    'SunlightAvg': '4.00',
                    'Location': 'Can - Whitecourt',
                    'Latitude': '55.17',
                    'Longitude': '-118.80',
                    'Declination': '17',
                    'TiltAngle': '45.00',
                    'DeclinationDirection': '1',
                },
                {
                    'State': 'Kuwait',
                    'City': 'Kuwait City',
                    'SunlightMin': '3.01',
                    'SunlightAvg': '6.50',
                    'Location': 'Kuwait - Kuwait City',
                    'Latitude': '29.36',
                    'Longitude': '47.97',
                    'Declination': '7',
                    'TiltAngle': '25.00',
                    'DeclinationDirection': '',
                },
            ]

        }
    }
    return jsonify(response_object), 200
