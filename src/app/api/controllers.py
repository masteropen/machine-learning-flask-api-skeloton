from flask import Blueprint, request, redirect, url_for
from joblib import load
from os import getcwd

# Define the blueprint 'api'
api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/predict', methods=['POST'])
def predict():
    if request.form['years_experience'] is None:
        return redirect(url_for('bad_request'))
    model = load(getcwd() + '/app/dumps/salary_model.joblib')
    salary = model.predict([[float(request.form['years_experience'])]])
    return {
        'code': 200,
        'salary': salary[0]
    }
