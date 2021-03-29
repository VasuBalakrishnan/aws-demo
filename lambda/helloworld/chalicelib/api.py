from chalice import app, Blueprint, BadRequestError
from datetime import datetime

myapi = app.Blueprint(__name__)

@myapi.route('/')
def index():
    myapi.current_app.log.debug('index call')
    return {'hello': 'world', 'time': datetime.now().isoformat() }


CITIES_TO_STATE = {
    'seattle': 'WA',
    'portland': 'OR'
}

@myapi.route('/cities/{city}')
def state_of_city(city):
    try:
        myapi.current_app.log.debug('state_of_city %s' % city)
        return {'state': CITIES_TO_STATE[city]}
    except KeyError:
        raise BadRequestError("Unknown city %s, valid choices are %s" % (
            city, ", ".join(CITIES_TO_STATE.keys())
        ))
