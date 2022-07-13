from flask import Blueprint, redirect, render_template, request
from .calculations import calc_fourfactors, predict_winner


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect('/predict')

@main.route('/predict')
def predict():
    return render_template('predict.html')

@main.route('/', methods=['POST'])
@main.route('/predict', methods=['POST'])
def upload_and_predict():

    box = {
        "h_fgm": int(request.form.get("h_fgm")),
        "h_fga": int(request.form.get("h_fga")),
        "h_3pm": int(request.form.get("h_3pm")),
        "h_ftm": int(request.form.get("h_ftm")),
        "h_fta": int(request.form.get("h_fta")),
        "h_trb": int(request.form.get("h_trb")),
        "h_orb": int(request.form.get("h_orb")),
        "h_tov": int(request.form.get("h_tov")),
        "a_fgm": int(request.form.get("a_fgm")),
        "a_fga": int(request.form.get("a_fga")),
        "a_3pm": int(request.form.get("a_3pm")),
        "a_ftm": int(request.form.get("a_ftm")),
        "a_fta": int(request.form.get("a_fta")),
        "a_trb": int(request.form.get("a_trb")),
        "a_orb": int(request.form.get("a_orb")),
        "a_tov": int(request.form.get("a_tov")),
        }
    X = calc_fourfactors(box)

    winner, proba = predict_winner(X)
    return render_template('predict.html', predicted=winner, proba=proba)


@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/fourfactors_predict')
def ff_predict():
    X = {
            'h_efg': float(request.form.get('h_efg')),
            'h_tov': float(request.form.get('h_tov')),
            'h_drp': float(request.form.get('h_drp')),
            'h_ftr': float(request.form.get('h_ftr')),
            'a_efg': float(request.form.get('a_efg')),
            'a_tov': float(request.form.get('a_tov')),
            'a_drp': float(request.form.get('a_drp')),
            'a_ftr': float(request.form.get('a_ftr'))
        }
    winner, proba = predict_winner(X)
    return render_template('predict.html', predicted=winner, proba=proba)