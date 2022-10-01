"""Calculations Module"""

import pickle
import pandas as pd


def calc_fourfactors(boxscore: dict) -> dict:
    """Calculate four factors for each team

    Args:
        boxscore (dict): dictionary of relevant boxscore data. Requires the following keys ->
         ['_fgm', '_3pm', '_fga', '_tov', '_ftm', '_fta', '_trb', '_orb']
         prefixed with 'h' and 'a' for home and away teams respectively.

    Returns:
        four factors (dict): dictionary of four factors values calculated from
        given boxscore
    """
    fourfactors = {}
    h_dreb = boxscore['h_trb'] - boxscore['h_orb']
    a_dreb = boxscore['a_trb'] - boxscore['a_orb']

    # Shooting : (FG + 0.5 * 3FG) / FGA
    fourfactors['h_efg'] = (boxscore['h_fgm'] + 0.5 * boxscore['h_3pm']) / boxscore['h_fga']
    fourfactors['a_efg'] = (boxscore['a_fgm'] + 0.5 * boxscore['a_3pm']) / boxscore['a_fga']

    # Turnovers : TOV / (FGA + 0.44 * FTA + TOV)
    fourfactors['h_tov'] = boxscore['h_tov'] / (boxscore['h_fga']
                                                + 0.44 * boxscore['h_fta']
                                                + boxscore['h_tov'])
    fourfactors['a_tov'] = boxscore['a_tov'] / (boxscore['a_fga']
                                                + 0.44 * boxscore['a_fta']
                                                + boxscore['h_tov'])

    # Rebounding : DRB / (Opp ORB + DRB)
    fourfactors['h_drb'] = h_dreb / (boxscore['a_orb'] + h_dreb)
    fourfactors['a_drb'] = a_dreb / (boxscore['h_orb'] + a_dreb)

    # Freethrows : FT / FGA
    fourfactors['h_ftr'] = boxscore['h_ftm'] / boxscore['h_fga']
    fourfactors['a_ftr'] = boxscore['a_ftm'] / boxscore['a_fga']

    return fourfactors


def predict_winner(fourfactors_dict: dict) -> tuple:
    """Return winner of game and probability of expected result

    Args:
        fourfactors_dict (dict): dictionary of four factors values (floats), with the
        following keys: ['h_efg', 'a_efg', 'h_tov', 'a_tov', 'h_drb', 'a_drb',
        'h_ftr', 'a_ftr']

    Returns:
        winner, proba (str, float): Tuple of the projected winner and model's
        probability of predicted outcome occurring.
    """
    # load model
    try:
        with open('nba_game_predictor/model.pickle', 'rb') as file:
            model = pickle.load(file)
    except FileNotFoundError:
        return 'Prediction model is missing', -1

    # predict
    fourfactors_df = pd.DataFrame(fourfactors_dict, index=[0]).astype(float)
    result = model.predict(fourfactors_df)[0]
    proba = round(model.predict_proba(fourfactors_df).max(), 3)
    if result == 1:
        return 'Home team', proba
    else:
        return 'Away team', proba
