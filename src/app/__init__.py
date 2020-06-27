from flask import Flask
from app.api.controllers import api

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Register blueprint(s)
app.register_blueprint(api)


# global routes
@app.errorhandler(400)
def bad_request(error):
    return {
        'code': 400,
        'name': error.name,
        'description': error.description
    }


@app.errorhandler(404)
def page_not_found(error):
    return {
        'code': 404,
        'name': error.name,
        'description': error.description
    }


@app.errorhandler(405)
def method_not_allowed(error):
    return {
        'code': 405,
        'name': error.name,
        'description': error.description
    }
