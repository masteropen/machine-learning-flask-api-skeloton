from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Happy to see you !'


# this an example of the exposed api to client(s)
@app.route('/predict', methods=['POST'])
def predict():
    return 'predict salary for an employee having ' + request.form['years_experience'] + ' years of experience'


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
